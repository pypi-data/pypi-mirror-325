from functools import partial
import os
import torch
import torch.nn as nn
import numpy as np
from auto_LiRPA.bound_general import BoundedModule

from smac import Scenario, HyperparameterOptimizationFacade
from smac.utils.configspace import get_config_hash

from CTRAIN.eval.eval import eval_acc, eval_model, eval_complete_abcrown
from CTRAIN.model_wrappers.configs import get_config_space


class CTRAINWrapper(nn.Module):
    
    def __init__(self, model: nn.Module, eps:float, input_shape: tuple, train_eps_factor=1, lr=0.0005, optimizer_func=torch.optim.Adam, bound_opts=dict(conv_mode='patches', relu='adaptive'), device='cuda', checkpoint_save_path=None):
        super(CTRAINWrapper, self).__init__()
        model = model.to(device)
        
        original_train = model.training
        self.original_model = model
        self.eps = eps
        self.train_eps = eps * train_eps_factor
        if isinstance(device, torch.device):
            self.device = device
        else:
            if device in ['cuda', 'cpu', 'mps']:
                self.device = torch.device(device)
            else:
                print("Unknown device - falling back to device CPU!")
                self.device = torch.device('cpu')
        
        if len(input_shape) < 4:
            input_shape = [1, *input_shape]
        model.eval()
        example_input = torch.ones(input_shape, device=device)
        self.n_classes = len(model(example_input)[0])
        self.bound_opts = bound_opts
        self.bounded_model = BoundedModule(model=self.original_model, global_input=example_input, bound_opts=bound_opts, device=device)
        self.input_shape = input_shape
        
        self.optimizer_func = optimizer_func
        self.optimizer = optimizer_func(self.bounded_model.parameters(), lr=lr)
        
        self.epoch = 0
        
        if original_train:
            self.original_model.train()
            self.bounded_model.train()
        
        self.checkpoint_path = checkpoint_save_path
        if checkpoint_save_path is not None:
            os.makedirs(self.checkpoint_path, exist_ok=True)
    
    def train(self):
        self.original_model.train()
        self.bounded_model.train()
    
    def eval(self):
        self.original_model.train()
        self.bounded_model.train()
    
    def forward(self, x):
        return self.bounded_model(x)
    
    def evaluate(self, test_loader, test_samples=np.inf):
        eps_std = self.eps / test_loader.std if test_loader.normalised else torch.tensor(self.eps)
        eps_std = torch.reshape(eps_std, (*eps_std.shape, 1, 1))
        return eval_model(self.bounded_model, test_loader, n_classes=self.n_classes, eps=eps_std, test_samples=test_samples, method='ADAPTIVE', device=self.device)

    def evaluate_complete(self, test_loader, test_samples=np.inf, timeout=1000, no_cores=4, abcrown_batch_size=512):
        eps_std = self.eps / test_loader.std if test_loader.normalised else self.eps
        eps_std = torch.reshape(eps_std, (*eps_std.shape, 1, 1))
        std_acc = eval_acc(self.bounded_model, test_loader=test_loader, test_samples=test_samples)
        certified_acc, adv_acc = eval_complete_abcrown(
            model=self.bounded_model,
            eps_std=eps_std,
            data_loader=test_loader,
            n_classes=self.n_classes,
            input_shape=self.input_shape,
            test_samples=test_samples,
            timeout=timeout,
            no_cores=no_cores,
            abcrown_batch_size=abcrown_batch_size,
            device=self.device
        )
        return std_acc, certified_acc, adv_acc
    
    def state_dict(self):
        return self.bounded_model.state_dict()
    
    def load_state_dict(self, state_dict, strict = True):
        return self.bounded_model.load_state_dict(state_dict, strict)
    
    def parameters(self, recurse=True):
        return self.bounded_model.parameters(recurse=recurse)
    # TODO: Add onnx export/loading

    def resume_from_checkpoint(self, checkpoint_path:str, train_loader, val_loader=None):
        checkpoint = torch.load(checkpoint_path)
        model_state_dict = checkpoint['model_state_dict']
        self.load_state_dict(model_state_dict)
        self.epoch = checkpoint['epoch']
        optimizer_state_dict = checkpoint['optimizer_state_dict']
        self.optimizer.load_state_dict(optimizer_state_dict)
        self.train_model(train_loader, val_loader, start_epoch=self.epoch)

    
    
    def hpo(self, train_loader, val_loader, budget=5*24*60*60, defaults=dict(), eval_samples=1000, output_dir='./smac_hpo', include_nat_loss=True, include_adv_loss=True, include_cert_loss=True):
        os.makedirs(output_dir, exist_ok=True)
        if os.listdir(output_dir):
            assert False, 'Output directory for HPO is not empty!'
        
        os.makedirs(f'{output_dir}/nets', exist_ok=True)
        os.makedirs(f'{output_dir}/smac/', exist_ok=True)

        eps_std = self.eps / train_loader.std
        scenario = Scenario(
            configspace=get_config_space(self, self.num_epochs, eps_std, defaults=defaults),
            walltime_limit=budget,
            n_trials=np.inf,
            output_directory=f'{output_dir}/smac/',
            use_default_config=True if len(defaults.values()) > 0 else False
        )
        initial_design = HyperparameterOptimizationFacade.get_initial_design(scenario, n_configs_per_hyperparamter=1)
        smac = HyperparameterOptimizationFacade(
            scenario,
            partial(self._hpo_runner, epochs=self.num_epochs, train_loader=train_loader, val_loader=val_loader, cert_eval_samples=eval_samples, output_dir=output_dir, include_nat_loss=include_nat_loss, include_adv_loss=include_adv_loss, include_cert_loss=include_cert_loss),
            initial_design=initial_design,
            overwrite=True,
        )

        inc = smac.optimize()
        
        config_hash = get_config_hash(inc, 32)
        self.load_state_dict(torch.load(f'{output_dir}/nets/{config_hash}.pt'))

        return inc

    def _hpo_runner(self, config, seed, epochs, train_loader, val_loader, output_dir, cert_eval_samples=1000):
        raise NotImplementedError('HPO can only be run on the concrete Wrappers!')


