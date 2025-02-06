import torch

from CTRAIN.bound import bound_ibp, bound_crown_ibp
from CTRAIN.train.certified.losses import get_loss_from_bounds

# TODO: This should probably only return CROWN IBP Loss
def get_crown_ibp_loss(hardened_model, ptb, data, target, n_classes, criterion, beta, return_bounds=False, return_stats=True):
    ilb, iub = bound_ibp(
        model=hardened_model,
        ptb=ptb,
        data=data,
        target=target,
        n_classes=n_classes,
        bound_upper=False
    )
    if beta < 1e-5:
        lb = ilb
    else:
        # Attention: We have to reuse the input here. Otherwise the memory requirements become too large!
        # Input is reused from above bound_ibp call!
        clb, cub = bound_crown_ibp(
            model=hardened_model,
            ptb=ptb,
            data=data,
            target=target,
            n_classes=n_classes,
            reuse_input=True,
            bound_upper=False
        )
        
        lb = clb * beta + ilb * (1 - beta)

    certified_loss = get_loss_from_bounds(lb, criterion)
    
    return_tuple = (certified_loss,)
    
    if return_bounds:
        return_tuple = return_tuple + (lb, None)
    if return_stats:
        robust_err = torch.sum((lb < 0).any(dim=1)).item() / data.size(0)
        return_tuple = return_tuple + (robust_err,)
    
    return return_tuple