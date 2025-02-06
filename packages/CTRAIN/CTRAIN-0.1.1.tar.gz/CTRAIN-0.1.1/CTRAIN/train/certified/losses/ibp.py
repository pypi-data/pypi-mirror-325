import torch
from CTRAIN.bound import bound_ibp
from CTRAIN.train.certified.losses import get_loss_from_bounds

def get_ibp_loss(hardened_model, ptb, data, target, n_classes, criterion, return_bounds=False, return_stats=False):
    lb, ub = bound_ibp(
        model=hardened_model,
        ptb=ptb,
        data=data,
        target=target,
        n_classes=n_classes,
    )
    certified_loss = get_loss_from_bounds(lb, criterion)
    
    return_tuple = (certified_loss,)
    
    if return_bounds:
        return_tuple = return_tuple + (lb, ub)
    if return_stats:
        robust_err = torch.sum((lb < 0).any(dim=1)).item() / data.size(0)
        return_tuple = return_tuple + (robust_err,)
    
    return return_tuple
