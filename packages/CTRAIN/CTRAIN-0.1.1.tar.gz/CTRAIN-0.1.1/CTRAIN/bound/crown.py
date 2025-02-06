import torch
from auto_LiRPA import BoundedTensor

from CTRAIN.util import construct_c

# Uses CROWN bounds throughout all intermediate layers and the final layer. 
def bound_crown(model, ptb, data, target, n_classes=10, bound_upper=False, reuse_input=False):
    data = BoundedTensor(data, ptb=ptb)
    c = construct_c(data, target, n_classes)
    if reuse_input:
        bound_input = None
    else:
        bound_input = (data,)
    lb, ub = model.compute_bounds(x=bound_input, IBP=False, method="CROWN", C=c, bound_upper=bound_upper)
    return lb, ub

# CROWN-IBP uses IBP bounds for all intermediate layers and CROWN bounds for the last one
def bound_crown_ibp(model, ptb, data, target, n_classes=10, bound_upper=False, reuse_input=False):
    data = BoundedTensor(data, ptb=ptb)
    c = construct_c(data, target, n_classes)
    if reuse_input:
        bound_input = None
    else:
        bound_input = (data,)
    lb, ub = model.compute_bounds(x=bound_input, IBP=False, method="CROWN-IBP", C=c, bound_upper=bound_upper)
    return lb, ub