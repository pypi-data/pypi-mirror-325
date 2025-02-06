import torch
from auto_LiRPA import BoundedTensor
from CTRAIN.util import construct_c

def bound_ibp(model, ptb, data, target, n_classes=10, bound_upper=False, reuse_input=False):
    data = BoundedTensor(data, ptb=ptb)
    if target is not None:
        c = construct_c(data, target, n_classes)
    else:
        c = None
    if reuse_input:
        bound_input = None
    else:
        bound_input = (data,)
    lb, ub = model.compute_bounds(x=bound_input, IBP=True, method="IBP", C=c, bound_upper=bound_upper)
    return lb, ub