import torch
import torch.nn as nn
from CTRAIN.bound import *

def get_loss_from_bounds(lb, criterion):
    lb_padded = torch.cat((torch.zeros(size=(lb.size(0),1), dtype=lb.dtype, device=lb.device), lb), dim=1)
    fake_labels = torch.zeros(size=(lb.size(0),), dtype=torch.int64, device=lb.device)
    certified_loss = criterion(-lb_padded, fake_labels).mean()
    return certified_loss

def get_bound_by_name(bounding_method='IBP', *args, **kwargs):
    if bounding_method.lower() == 'ibp':
        return bound_ibp(*args, **kwargs)
    elif bounding_method.lower() == 'crown_ibp':
        return bound_crown_ibp(*args, **kwargs)
    elif bounding_method.lower() == 'crown':
        return bound_crown(*args, **kwargs)
    elif bounding_method.lower() == 'sabr':
        return bound_sabr(*args, **kwargs)
    elif bounding_method.lower() == 'taps':
        return bound_taps(*args, **kwargs)
    else:
        assert False, f"Unsupported bounding method: {bounding_method}"
