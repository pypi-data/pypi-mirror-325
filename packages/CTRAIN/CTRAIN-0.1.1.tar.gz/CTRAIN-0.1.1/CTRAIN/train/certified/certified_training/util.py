import copy
import types
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

from auto_LiRPA.bound_general import BoundedModule

from auto_LiRPA.operators.normalization import BoundBatchNormalization

from auto_LiRPA.operators.solver_utils import grb

from auto_LiRPA.linear_bound import LinearBound

from auto_LiRPA.operators.constant import BoundConstant

from auto_LiRPA.operators.leaf import BoundParams

from auto_LiRPA.patches import Patches, inplace_unfold

from auto_LiRPA.operators.base import Interval


def split_network(model, block_sizes, network_input, device):
    # TODO: Add assertions for robustness
    start = 0
    original_blocks = []
    network_input = network_input.to(device)
    for size in block_sizes:
        end = start + size
        abs_block = nn.Sequential(model.layers[start:end])
        original_blocks.append(abs_block)
        
        output_shape = abs_block(network_input).shape
        network_input = torch.zeros(output_shape).to(device)
        
        start = end
    return original_blocks

def freeze_batch_norm(model):
    def _check_unused_mean_or_var(self):
        if not hasattr(self, 'frozen') or not self.frozen:
            # Check if either mean or var is opted out
            if not self.use_mean:
                self.current_mean = torch.zeros_like(self.current_mean)
            if not self.use_var:
                self.current_var = torch.ones_like(self.current_var)
        else:
            pass

    def forward(self, x, w, b, m, v):
        if len(x.shape) == 2:
            self.patches_start = False
        if self.training and not self.frozen:
            dim = [0] + list(range(2, x.ndim))
            self.current_mean = x.mean(dim)
            self.current_var = x.var(dim, unbiased=False)
        else:
            self.current_mean = m.data
            self.current_var = v.data
        self._check_unused_mean_or_var()
        if not self.use_affine:
            w = torch.ones_like(w)
            b = torch.zeros_like(b)
        result = F.batch_norm(x, m, v, w, b, self.training, self.momentum, self.eps)
        if not self.use_mean or not self.use_var:
            # If mean or variance is disabled, recompute the output from self.current_mean
            # and self.current_var instead of using standard F.batch_norm.
            w = w / torch.sqrt(self.current_var + self.eps)
            b = b - self.current_mean * w
            shape = (1, -1) + (1,) * (x.ndim - 2)
            result = w.view(*shape) * x + b.view(*shape)
        return result
    
    for module in model.modules():
        if isinstance(module, BoundBatchNormalization):
            assert not hasattr(module, 'orig_momentum'), "Batch Norm is already frozen! Please run unfreeze_batch_norm before trying to freeze it!"
            module.orig_momentum = module.momentum
            module.momentum = 0.0
            module._check_unused_mean_or_var = types.MethodType(_check_unused_mean_or_var, module)
            module.forward = types.MethodType(forward, module)
            module.frozen = True
            module.use_mean = False
            module.use_var = False

def unfreeze_batch_norm(model):
    for module in model.modules():
        if isinstance(module, BoundBatchNormalization):
            assert hasattr(module, 'orig_momentum'), "Please run freeze_batch_norm before trying to unfreeze it"
            module.momentum = module.orig_momentum
            del module.orig_momentum
            module.use_mean = True
            module.use_var = True
            module.frozen = False


def reset_batch_norms_to_data_statistics(model, dataloader, device='cuda'):
    '''
    Use population statistics to reset the BN layers in the model.
    '''
    model.to(device)
    bn_list = [m for m in model.modules() if isinstance(m, BoundBatchNormalization)]
    if len(bn_list) == 0:
        return model
    model.train()
    momentum_list = [m.momentum for m in bn_list]
    num_batches_tracked = 0
    for x, _ in dataloader:
        x = x.to(device)
        num_batches_tracked += 1
        with torch.no_grad():
            for m in bn_list:
                m.momentum = 1 / num_batches_tracked
            model(x)
    for m in bn_list:
        m.momentum = momentum_list.pop(0)
