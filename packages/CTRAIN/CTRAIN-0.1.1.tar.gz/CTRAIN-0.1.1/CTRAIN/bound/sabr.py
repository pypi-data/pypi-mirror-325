from auto_LiRPA.perturbations import PerturbationLpNorm

import numpy as np
import torch

from CTRAIN.bound.ibp import bound_ibp
from CTRAIN.attacks import pgd_attack


def bound_sabr(hardened_model, original_model, data, target, eps, subselection_ratio, device='cuda', n_classes=10, x_L=None, x_U=None, data_min=None, data_max=None, n_steps=8, step_size=.5, restarts=1, early_stopping=True, intermediate_bound_model=None, decay_factor=0.1, decay_checkpoints=(4,7), return_adv_output=False):
    hardened_model.eval()
    original_model.eval()
    
    propagation_inputs, tau, x_adv = get_propagation_region(
        model=hardened_model,
        data=data,
        data_min=data_min,
        data_max=data_max,
        target=target,
        eps=eps if (x_L is None and x_U is None) else None,
        subselection_ratio=subselection_ratio,
        n_steps=n_steps,
        step_size=step_size,
        restarts=restarts,
        early_stopping=early_stopping,
        x_L=x_L,
        x_U=x_U,
        decay_checkpoints=decay_checkpoints, 
        decay_factor=decay_factor
    )
    
    hardened_model.train()
    original_model.train()
    
    ptb = PerturbationLpNorm(eps=tau, norm=np.inf, x_L=torch.clamp(propagation_inputs - tau, data_min, data_max).to(device), x_U=torch.clamp(propagation_inputs + tau, data_min, data_max).to(device))
    
    # Pass input through network to set batch statistics
    adv_output = hardened_model(x_adv)
    
    lb, ub = bound_ibp(
        model=hardened_model if intermediate_bound_model is None else intermediate_bound_model,
        ptb=ptb,
        data=propagation_inputs,
        target=target if intermediate_bound_model is None else None,
        n_classes=n_classes,
        bound_upper=True,
        reuse_input=False
    )
    
    if return_adv_output:
        return lb, ub, adv_output
    return lb, ub

def get_propagation_region(model, data, target, subselection_ratio, step_size, n_steps, restarts, x_L=None, x_U=None, data_min=None, data_max=None, eps=None, early_stopping=True, decay_factor=.1, decay_checkpoints=(4, 7)):
    device = torch.device("cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu")
    assert (x_L is None and x_U is None and eps is not None) or (x_L is not None and x_U is not None and eps is None), "Please only provide epsilon value OR upper and lower input bounds"
    tau = None
    if eps.all() and data is not None:
        x_L=torch.clamp(data - eps, data_min, data_max).to(device)
        x_U=torch.clamp(data + eps, data_min, data_max).to(device)
    else:
        eps = torch.max((x_U - x_L))
    
    tau =  subselection_ratio * eps

    x_adv = pgd_attack(
        model=model,
        data=data,
        target=target,
        x_L=x_L,
        x_U=x_U,
        n_steps=n_steps,
        step_size=step_size,
        restarts=restarts,
        early_stopping=early_stopping,
        device=device,
        decay_checkpoints=decay_checkpoints,
        decay_factor=decay_factor
    )
    
    propagation_inputs = torch.clamp(x_adv, x_L + tau, x_U - tau) # called midpoints in SABR code
    tau = torch.tensor(tau, device=device)
    return propagation_inputs, tau, x_adv