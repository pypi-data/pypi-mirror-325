import copy
import torch

from smac.utils.configspace import get_config_hash

from CTRAIN.model_wrappers.model_wrapper import CTRAINWrapper
from CTRAIN.train.certified.certified_training import crown_ibp_train_model
from CTRAIN.util.util import seed_ctrain

class CrownIBPModelWrapper(CTRAINWrapper):
    
    def __init__(self, model, input_shape, eps, num_epochs, train_eps_factor=1, optimizer_func=torch.optim.Adam, lr=0.0005, warm_up_epochs=1, ramp_up_epochs=70,
                 lr_decay_factor=.2, lr_decay_milestones=(80, 90), gradient_clip=10, l1_reg_weight=0.000001,
                 shi_reg_weight=.5, shi_reg_decay=True, start_kappa=1, end_kappa=0, start_beta=1, end_beta=0, checkpoint_save_path=None,
                 bound_opts=dict(conv_mode='patches', relu='adaptive'), device=torch.device('cuda'),
                 ):
        super().__init__(model, eps, input_shape, train_eps_factor, lr, optimizer_func, bound_opts, device, checkpoint_save_path=checkpoint_save_path)
        self.cert_train_method = 'crown_ibp'
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
        self.start_kappa = start_kappa
        self.end_kappa = end_kappa
        self.start_beta = start_beta
        self.end_beta = end_beta
        self.optimizer_func = optimizer_func
        
    
    def train_model(self, train_loader, val_loader=None):
        eps_std = self.train_eps / train_loader.std if train_loader.normalised else torch.tensor(self.train_eps)

        eps_std = torch.reshape(eps_std, (*eps_std.shape, 1, 1))
        trained_model = crown_ibp_train_model(
            original_model=self.original_model,
            hardened_model=self.bounded_model,
            train_loader=train_loader,
            val_loader=val_loader,
            num_epochs=self.num_epochs,
            eps=self.train_eps,
            eps_std=eps_std,
            eps_schedule=(self.warm_up_epochs, self.ramp_up_epochs),
            eps_scheduler_args={'start_kappa': self.start_kappa, 'end_kappa': self.end_kappa, 'start_beta': self.start_beta, 'end_beta': self.end_beta},
            optimizer=self.optimizer,
            lr_decay_schedule=self.lr_decay_milestones,
            lr_decay_factor=self.lr_decay_factor,
            n_classes=self.n_classes,
            gradient_clip=self.gradient_clip,
            l1_regularisation_weight=self.l1_reg_weight,
            shi_regularisation_weight=self.shi_reg_weight,
            shi_reg_decay=self.shi_reg_decay,
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

        model_wrapper = CrownIBPModelWrapper(
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
            start_kappa=config['crown_ibp:start_kappa'],
            end_kappa=config['crown_ibp:end_kappa'] * config['crown_ibp:start_kappa'],
            start_beta=config['crown_ibp:start_beta'],
            end_beta=config['crown_ibp:end_beta'],
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