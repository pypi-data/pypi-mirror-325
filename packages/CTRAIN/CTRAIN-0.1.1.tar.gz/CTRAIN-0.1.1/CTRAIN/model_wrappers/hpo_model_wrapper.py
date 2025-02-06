import copy
from functools import partial
import math
import os
import numpy as np
from smac import HyperparameterOptimizationFacade, Scenario
import torch

from smac.utils.configspace import get_config_hash

from CTRAIN.model_wrappers.configs import get_combined_config_space
from CTRAIN.model_wrappers.model_wrapper import CTRAINWrapper
from CTRAIN.model_wrappers.shi_ibp_model_wrapper import ShiIBPModelWrapper
from CTRAIN.model_wrappers.crown_ibp_model_wrapper import CrownIBPModelWrapper
from CTRAIN.model_wrappers.sabr_model_wrapper import SABRModelWrapper
from CTRAIN.model_wrappers.mtl_ibp_model_wrapper import MTLIBPModelWrapper
from CTRAIN.model_wrappers.staps_model_wrapper import STAPSModelWrapper
from CTRAIN.model_wrappers.taps_model_wrapper import TAPSModelWrapper
from CTRAIN.train.certified.certified_training import shi_train_model
from CTRAIN.util import seed_ctrain

class HPOModelWrapper(CTRAINWrapper):
    
    def __init__(self, model, input_shape, eps, num_epochs, included_methods=['shi', 'crown_ibp', 'sabr', 'mtl_ibp', 'taps', 'staps'], 
                 train_eps_factor=1, checkpoint_save_path=None,
                 bound_opts=dict(conv_mode='patches', relu='adaptive'), device=torch.device('cuda'),
                 ):
        super().__init__(model, eps, input_shape, train_eps_factor, bound_opts, device, checkpoint_save_path=checkpoint_save_path)
        self.cert_train_method = 'hpo'
        self.num_epochs = num_epochs
        self.included_methods = included_methods
        
    
    def train_model(self, train_loader, val_loader=None):
        raise NotImplementedError('This Wrapper can only be used to find the ideal model wrapper - not for training itself!')
    

    def hpo(self, train_loader, val_loader, budget=5*24*60*60, defaults=dict(), output_dir='./smac_hpo'):
        os.makedirs(output_dir, exist_ok=True)
        if os.listdir(output_dir):
            assert False, 'Output directory for HPO is not empty!'
        
        os.makedirs(f'{output_dir}/nets', exist_ok=True)
        os.makedirs(f'{output_dir}/smac/', exist_ok=True)

        eps_std = self.eps / train_loader.std
        scenario = Scenario(
            configspace=get_combined_config_space(self.num_epochs, eps_std, defaults=defaults, included_methods=self.included_methods),
            walltime_limit=budget,
            n_trials=np.inf,
            output_directory=f'{output_dir}/smac/',
            use_default_config=True
        )
        initial_design = HyperparameterOptimizationFacade.get_initial_design(scenario, n_configs_per_hyperparamter=1)
        smac = HyperparameterOptimizationFacade(
            scenario,
            partial(self._hpo_runner, epochs=self.num_epochs, train_loader=train_loader, val_loader=val_loader, output_dir=output_dir),
            initial_design=initial_design,
            overwrite=True,
        )

        inc = smac.optimize()

        if inc['optimizer_func'] == 'adam':
            optimizer_func = torch.optim.Adam
        elif inc['optimizer_func'] == 'radam':
            optimizer_func = torch.optim.RAdam
        if inc['optimizer_func'] == 'adamw':
            optimizer_func = torch.optim.AdamW
        
        lr_decay_milestones = [
            inc['warm_up_epochs'] + inc['ramp_up_epochs'] + inc['lr_decay_epoch_1'],
            inc['warm_up_epochs'] + inc['ramp_up_epochs'] + inc['lr_decay_epoch_1'] + inc['lr_decay_epoch_2']
        ]

        model_wrapper = self._get_wrapper_from_config(
            config=inc, 
            epochs=self.num_epochs,
            optimizer_func=optimizer_func,
            lr_decay_milestones=lr_decay_milestones
        )
        
        config_hash = get_config_hash(inc, 32)
        model_wrapper.load_state_dict(torch.load(f'{output_dir}/nets/{config_hash}.pt'))

        return model_wrapper, inc

    def _hpo_runner(self, config, seed, epochs, train_loader, val_loader, output_dir, cert_eval_samples=1000):
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

        model_wrapper = self._get_wrapper_from_config(
            config=config, 
            epochs=epochs,
            optimizer_func=optimizer_func,
            lr_decay_milestones=lr_decay_milestones
        )

        model_wrapper.train_model(train_loader=train_loader)
        torch.save(model_wrapper.state_dict(), f'{output_dir}/nets/{config_hash}.pt')
        model_wrapper.eval()
        std_acc, cert_acc, adv_acc = model_wrapper.evaluate(test_loader=val_loader, test_samples=cert_eval_samples)


        return -(std_acc + cert_acc + adv_acc), {'nat_acc': std_acc, 'adv_acc': adv_acc, 'cert_acc': cert_acc} 


    def _get_wrapper_from_config(self, config, epochs, optimizer_func, lr_decay_milestones):
        if config['cert_train_method'] == 'shi':
            model_wrapper = ShiIBPModelWrapper(
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
                start_kappa=config['shi:start_kappa'],
                end_kappa=config['shi:end_kappa'] * config['shi:start_kappa'],
            )
        elif config['cert_train_method'] == 'crown_ibp':
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
        elif config['cert_train_method'] == 'sabr':
            model_wrapper = SABRModelWrapper(
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
                sabr_subselection_ratio=config['sabr:subselection_ratio'],
                pgd_alpha=config['sabr:pgd_alpha'],
                pgd_early_stopping=False,
                pgd_restarts=config['sabr:pgd_restarts'],
                pgd_steps=config['sabr:pgd_steps'],
                pgd_decay_milestones=()
            )
        elif config['cert_train_method'] == 'mtl_ibp':
            model_wrapper = MTLIBPModelWrapper(
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
                mtl_ibp_alpha=config['mtl_ibp:mtl_ibp_alpha'],
                pgd_alpha=config['mtl_ibp:pgd_alpha'],
                pgd_early_stopping=False,
                pgd_restarts=config['mtl_ibp:pgd_restarts'],
                pgd_steps=config['mtl_ibp:pgd_steps'],
                pgd_eps_factor=config['mtl_ibp:mtl_ibp_eps_factor'],
                pgd_decay_milestones=()
            )
        elif config['cert_train_method'] == 'taps':
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
                block_sizes=block_sizes
            )
        elif config['cert_train_method'] == 'staps':
            model_wrapper = STAPSModelWrapper(
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
                sabr_subselection_ratio=config['staps:sabr:subselection_ratio'],
                sabr_pgd_alpha=config['staps:sabr:pgd_alpha'],
                sabr_pgd_early_stopping=False,
                sabr_pgd_restarts=config['staps:sabr:pgd_restarts'],
                sabr_pgd_steps=config['staps:sabr:pgd_steps'],
                sabr_pgd_decay_milestones=(),
                pgd_alpha=config['staps:pgd_alpha'],
                pgd_restarts=config['staps:pgd_restarts'],
                pgd_steps=config['staps:pgd_steps'],
                gradient_expansion_alpha=config['staps:gradient_expansion_alpha'],
                pgd_early_stopping=False,
                pgd_decay_steps=(),
                block_sizes=block_sizes
            )
        return model_wrapper