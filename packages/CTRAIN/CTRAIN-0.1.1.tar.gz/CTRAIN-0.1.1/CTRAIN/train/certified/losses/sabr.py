import torch
from CTRAIN.bound import bound_sabr
from CTRAIN.train.certified.losses import get_loss_from_bounds

def get_sabr_loss(hardened_model, original_model, data, target, eps, subselection_ratio, criterion, device='cuda', 
                  n_classes=10, x_L=None, x_U=None, data_min=None, data_max=None, pgd_steps=8, pgd_step_size=.5, pgd_restarts=1, pgd_early_stopping=True, pgd_decay_factor=.1, pgd_decay_checkpoints=(4,7), return_stats=False, return_bounds=False, **kwargs):
    lb, ub, adv_output = bound_sabr(
        hardened_model=hardened_model,
        original_model=original_model,
        data=data,
        data_min=data_min,
        data_max=data_max,
        target=target,
        eps=eps,
        subselection_ratio=subselection_ratio,
        device=device,
        n_classes=n_classes,
        x_L=x_L,
        x_U=x_U,
        n_steps=pgd_steps,
        step_size=pgd_step_size,
        restarts=pgd_restarts,
        early_stopping=pgd_early_stopping,
        decay_checkpoints=pgd_decay_checkpoints, 
        decay_factor=pgd_decay_factor,
        return_adv_output=True
    )
    loss = get_loss_from_bounds(lb, criterion=criterion)
    
    return_tuple = (loss,)
    
    if return_bounds:
        assert False, "Return bounds is not implemented for MTL-IBP"
    elif return_stats:
        robust_err = torch.sum((lb < 0).any(dim=1)).item() / data.size(0)
        adv_err = torch.sum(torch.argmax(adv_output, dim=1) != target).item() / data.size(0)
        return_tuple = return_tuple + (robust_err, adv_err)
    
    return return_tuple
