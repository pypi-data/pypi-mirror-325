import torch

from CTRAIN.bound.taps import GradExpander
from CTRAIN.bound import bound_taps
from CTRAIN.train.certified.losses import get_loss_from_bounds


def get_taps_loss(original_model, hardened_model, bounded_blocks, criterion, data, target, n_classes, ptb, device='cuda', pgd_steps=8, pgd_restarts=1, 
                  pgd_step_size=None, pgd_decay_factor=.2, pgd_decay_checkpoints=(5,7), gradient_link_thresh=.5,
                  gradient_link_tolerance=1e-05, gradient_expansion_alpha=5, propagation="IBP", sabr_args=None, return_bounds=False, return_stats=False):
    assert len(bounded_blocks) == 2, "Split not supported!"
    
    taps_bound, ibp_bound = bound_taps(
        original_model=original_model,
        hardened_model=hardened_model,
        bounded_blocks=bounded_blocks,
        data=data,
        target=target,
        n_classes=n_classes,
        ptb=ptb,
        device=device,
        pgd_steps=pgd_steps,
        pgd_restarts=pgd_restarts,
        pgd_step_size=pgd_step_size, 
        pgd_decay_factor=pgd_decay_factor,
        pgd_decay_checkpoints=pgd_decay_checkpoints,
        gradient_link_thresh=gradient_link_thresh,
        gradient_link_tolerance=gradient_link_tolerance,
        propagation=propagation,
        sabr_args=sabr_args
    )
        
    taps_loss = get_loss_from_bounds(taps_bound, criterion)
    ibp_loss = get_loss_from_bounds(ibp_bound, criterion)
    
    loss = GradExpander.apply(taps_loss, gradient_expansion_alpha) * ibp_loss
    
    return_tuple = (loss,)
    
    if return_bounds:
        return_tuple = return_tuple + (taps_bound, None)
    if return_stats:
        robust_err = torch.sum((taps_bound < 0).any(dim=1)).item() / data.size(0)
        return_tuple = return_tuple + (robust_err,)

    return return_tuple
