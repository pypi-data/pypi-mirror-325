import torch
import numpy as np

from CTRAIN.attacks import pgd_attack
from CTRAIN.train.certified.losses.ibp import get_ibp_loss

def get_mtl_ibp_loss(hardened_model, original_model, ptb, data, target, n_classes, criterion, alpha, return_bounds=False, return_stats=False, restarts=1, step_size=.2, n_steps=200, pgd_ptb=None, early_stopping=False, decay_checkpoints=(), decay_factor=.1, device='cuda'):    
    hardened_model.eval()
    original_model.eval()
    x_adv = pgd_attack(
        model=hardened_model,
        data=data,
        target=target,
        x_L=pgd_ptb.x_L,
        x_U=pgd_ptb.x_U,
        restarts=restarts,
        step_size=step_size,
        n_steps=n_steps,
        early_stopping=early_stopping,
        device=device,
        decay_factor=decay_factor,
        decay_checkpoints=decay_checkpoints
    )
    
    hardened_model.train()
    original_model.train()
    
    adv_output = hardened_model(x_adv)
    adv_loss = criterion(adv_output, target).mean()

    robust_loss, lb, ub = get_ibp_loss(
        hardened_model=hardened_model,
        ptb=ptb,
        data=data,
        target=target,
        n_classes=n_classes,
        criterion=criterion,
        return_bounds=True
    )
    
    loss = alpha * robust_loss + (1 - alpha) * adv_loss
    
    return_tuple = (loss,)
    
    if return_bounds:
        assert False, "Return bounds is not implemented for MTL-IBP"
    elif return_stats:
        robust_err = torch.sum((lb < 0).any(dim=1)).item() / data.size(0)
        adv_err = torch.sum(torch.argmax(adv_output, dim=1) != target).item() / data.size(0)
        return_tuple = return_tuple + (robust_err, adv_err)
    
    return return_tuple


# def get_cc_ibp_loss(hardened_model, ptb, data, target, n_classes, criterion, alpha, return_bounds=False, restarts=1, step_size=.2, n_steps=200, early_stopping=False):
#     # TODO: use different (higher) eps for PGD
    
#     x_adv = pgd_attack(
#         model=hardened_model,
#         data=data,
#         target=target,
#         x_L=ptb.x_L,
#         x_U=ptb.x_U,
#         restarts=restarts,
#         step_size=step_size,
#         n_steps=n_steps,
#         early_stopping=early_stopping
#     )
    
#     # Pass x_adv through model s.t. IBP uses batch norm statistics from x_adv
#     adv_pred = hardened_model(x_adv)
#     adv_lb = get
    
        
#     ibp_lb, ibp_up = bound_ibp(
#         model=hardened_model,
#         ptb=ptb,
#         data=data,
#         target=target,
#         n_classes=n_classes,
#     )

    
#     if return_bounds:
#         assert False, "Return bounds is not implemented for MTL-IBP"
#     else:
#         return (1-alpha) * adv_loss + alpha * certified_loss