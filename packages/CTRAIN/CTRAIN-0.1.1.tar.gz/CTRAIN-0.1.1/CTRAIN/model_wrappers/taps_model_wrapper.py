import math
import torch
import copy

from smac.utils.configspace import get_config_hash

from auto_LiRPA.bound_general import BoundedModule
from CTRAIN.model_wrappers.model_wrapper import CTRAINWrapper
from CTRAIN.train.certified.certified_training import taps_train_model
from CTRAIN.train.certified.certified_training.util import split_network
from CTRAIN.util import seed_ctrain

class TAPSModelWrapper(CTRAINWrapper):
    
    def __init__(self, model, input_shape, eps, num_epochs, train_eps_factor=1, optimizer_func=torch.optim.Adam, lr=0.0005, warm_up_epochs=1, ramp_up_epochs=70,
                 lr_decay_factor=.2, lr_decay_milestones=(80, 90), gradient_clip=10, l1_reg_weight=0.000001,
                 shi_reg_weight=.5, shi_reg_decay=True, pgd_steps=8, 
                 pgd_alpha=0.5, pgd_restarts=1, pgd_early_stopping=False, pgd_alpha_decay_factor=.1,
                 pgd_decay_steps=(4,7), block_sizes=None, gradient_expansion_alpha=5,
                 gradient_link_thresh=.5, gradient_link_tol=0.00001,
                 checkpoint_save_path=None,
                 bound_opts=dict(conv_mode='patches', relu='adaptive'), device=torch.device('cuda'),
                 ):
        super().__init__(model, eps, input_shape, train_eps_factor, lr, optimizer_func, bound_opts, device, checkpoint_save_path=checkpoint_save_path)
        self.cert_train_method = 'taps'
        self.num_epochs = num_epochs
        self.lr = lr
        self.warm_up_epochs = warm_up_epochs
        self.ramp_up_epochs = ramp_up_epochs
        self.lr_decay_factor = lr_decay_factor
        self.lr_decay_milestones = lr_decay_milestones
        self.gradient_clip = gradient_clip
        self.l1_reg_weight = l1_reg_weight
        self.shi_reg_weight = shi_reg_weight
        self.shi_reg_decay = shi_reg_decay
        self.optimizer_func = optimizer_func
        self.pgd_steps = pgd_steps
        self.pgd_alpha = pgd_alpha
        self.pgd_restarts = pgd_restarts
        self.pgd_early_stopping = pgd_early_stopping
        self.pgd_alpha_decay_factor = pgd_alpha_decay_factor
        self.pgd_decay_steps = pgd_decay_steps
        self.block_sizes = block_sizes
        self.gradient_expansion_alpha = gradient_expansion_alpha
        self.gradient_link_thresh = gradient_link_thresh
        self.gradient_link_tol = gradient_link_tol
        
        ori_train = self.original_model.training
        self.original_model.eval()
        self.bounded_model.eval()
        
        assert block_sizes is not None, "For TAPS training we require a network split!"
        dummy_input = torch.zeros(self.input_shape, device=device)
        blocks = split_network(self.original_model, block_sizes=block_sizes, network_input=dummy_input, device=device)
        if len(blocks) != 2:
            raise NotImplementedError("Currently we only support two blocks (feature extractor +  classifier) for TAPS/STAPS")
        features, classifier = blocks
        self.bounded_model.bounded_blocks = [
            BoundedModule(features, global_input=dummy_input, bound_opts=bound_opts, device=device),
            BoundedModule(classifier, global_input=torch.zeros_like(features(dummy_input), device=device), bound_opts=bound_opts, device=device)
        ]
        self.bounded_model.original_blocks = [features, classifier]
        
        if ori_train:
            self.original_model.train()
            self.bounded_model.train()
        
        
    
    def train_model(self, train_loader, val_loader=None, start_epoch=0):
        eps_std = self.train_eps / train_loader.std if train_loader.normalised else torch.tensor(self.train_eps)
        eps_std = torch.reshape(eps_std, (*eps_std.shape, 1, 1))
        trained_model = taps_train_model(
            original_model=self.original_model,
            hardened_model=self.bounded_model,
            train_loader=train_loader,
            val_loader=val_loader,
            num_epochs=self.num_epochs,
            eps=self.train_eps,
            eps_std=eps_std,
            eps_schedule=(self.warm_up_epochs, self.ramp_up_epochs),
            eps_scheduler_args={},
            optimizer=self.optimizer,
            lr_decay_schedule=self.lr_decay_milestones,
            lr_decay_factor=self.lr_decay_factor,
            n_classes=self.n_classes,
            gradient_clip=self.gradient_clip,
            l1_regularisation_weight=self.l1_reg_weight,
            shi_regularisation_weight=self.shi_reg_weight,
            shi_reg_decay=self.shi_reg_decay,
            gradient_expansion_alpha=self.gradient_expansion_alpha,
            taps_gradient_link_thresh=self.gradient_link_thresh,
            taps_gradient_link_tolerance=self.gradient_link_tol,
            taps_pgd_restarts=self.pgd_restarts,
            taps_pgd_step_size=self.pgd_alpha,
            taps_pgd_steps=self.pgd_steps,
            taps_pgd_decay_checkpoints=self.pgd_decay_steps,
            taps_pgd_decay_factor=self.pgd_alpha_decay_factor,
            start_epoch=start_epoch,
            results_path=self.checkpoint_path,
            device=self.device
        )
        
        return trained_model
    
    def _hpo_runner(self, config, seed, epochs, train_loader, val_loader, output_dir, cert_eval_samples=1000, include_nat_loss=True, include_adv_loss=True, include_cert_loss=True):
        config_hash = get_config_hash(config, 32)
        seed_ctrain(seed)

        if config['optimizer_func'] == 'adam':
            optimizer_func = torch.optim.Adam
        elif config['optimizer_func'] == 'radam':
            optimizer_func = torch.optim.RAdam
        if config['optimizer_func'] == 'adamw':
            optimizer_func = torch.optim.AdamW

        lr_decay_milestones = [
            config['warm_up_epochs'] + config['ramp_up_epochs'] + config['lr_decay_epoch_1'],
            config['warm_up_epochs'] + config['ramp_up_epochs'] + config['lr_decay_epoch_1'] + config['lr_decay_epoch_2']
        ]

        no_layers = len(self.original_model.layers)
        feature_extractor_size = math.ceil(config['taps:block_split_point'] * no_layers)
        classifier_size = no_layers - feature_extractor_size
        block_sizes = (feature_extractor_size, classifier_size)
                
        model_wrapper = TAPSModelWrapper(
            model=copy.deepcopy(self.original_model), 
            input_shape=self.input_shape,
            eps=self.eps,
            num_epochs=epochs, 
            bound_opts=self.bound_opts,
            checkpoint_save_path=None,
            device=self.device,
            train_eps_factor=config['train_eps_factor'],
            optimizer_func=optimizer_func,
            lr=config['learning_rate'],
            warm_up_epochs=config['warm_up_epochs'],
            ramp_up_epochs=config['ramp_up_epochs'],
            gradient_clip=10,
            lr_decay_factor=config['lr_decay_factor'],
            lr_decay_milestones=[epoch for epoch in lr_decay_milestones if epoch <= epochs],
            l1_reg_weight=config['l1_reg_weight'],
            shi_reg_weight=config['shi_reg_weight'],
            shi_reg_decay=config['shi_reg_decay'],
            pgd_alpha=config['taps:pgd_alpha'],
            pgd_restarts=config['taps:pgd_restarts'],
            pgd_steps=config['taps:pgd_steps'],
            gradient_expansion_alpha=config['taps:gradient_expansion_alpha'],
            pgd_early_stopping=False,
            pgd_decay_steps=(),
            block_sizes=block_sizes,
        )

        model_wrapper.train_model(train_loader=train_loader)
        torch.save(model_wrapper.state_dict(), f'{output_dir}/nets/{config_hash}.pt')
        model_wrapper.eval()
        std_acc, cert_acc, adv_acc = model_wrapper.evaluate(test_loader=val_loader, test_samples=cert_eval_samples)

        loss = 0
        if include_nat_loss:
            loss -= std_acc
        if include_adv_loss:
            loss -= adv_acc
        if include_cert_loss:
            loss -= cert_acc

        return loss, {'nat_acc': std_acc, 'adv_acc': adv_acc, 'cert_acc': cert_acc} 