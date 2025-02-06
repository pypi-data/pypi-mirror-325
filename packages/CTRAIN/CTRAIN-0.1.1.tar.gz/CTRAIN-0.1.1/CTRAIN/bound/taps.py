import math
import sys
import torch
import numpy as np
from auto_LiRPA import PerturbationLpNorm, BoundedTensor

from CTRAIN.bound import bound_ibp, bound_sabr
from CTRAIN.util import construct_c


def bound_taps(original_model, hardened_model, bounded_blocks, data, target, n_classes, ptb, device='cuda', pgd_steps=20, pgd_restarts=1, pgd_step_size=.2, 
               pgd_decay_factor=.2, pgd_decay_checkpoints=(5,7),
               gradient_link_thresh=.5, gradient_link_tolerance=1e-05, propagation="IBP", sabr_args=None):
    assert len(bounded_blocks) == 2, "Split not supported!"
    
    if propagation == 'IBP':
        lb, ub = bound_ibp(
            model=bounded_blocks[0],
            ptb=ptb,
            data=data,
            target=None,
            n_classes=n_classes,
        )
    if propagation == 'SABR':
        assert sabr_args is not None, "Need to Provide SABR arguments if you choose SABR for propagation"
        lb, ub = bound_sabr(
            # Intermediate Bound model instructs to return bounds after the first network block
            **{**sabr_args, "intermediate_bound_model": bounded_blocks[0], "return_adv_output": False},
        )
    
    with torch.no_grad():
        hardened_model.eval()
        original_model.eval()
        for block in bounded_blocks:
            block.eval()
        c = construct_c(data, target, n_classes)
        with torch.no_grad():
            grad_cleaner = torch.optim.SGD(hardened_model.parameters())
            adv_samples = _get_pivotal_points(bounded_blocks[1], lb, ub, pgd_steps, pgd_restarts, pgd_step_size, pgd_decay_factor, pgd_decay_checkpoints, n_classes, C=c)
            grad_cleaner.zero_grad()
            
        hardened_model.train()
        original_model.train()
        for block in bounded_blocks:
            block.train()
    
    pts = adv_samples[0].detach()
    pts = torch.transpose(pts, 0, 1)
    pts = RectifiedLinearGradientLink.apply(lb.unsqueeze(0), ub.unsqueeze(0), pts, gradient_link_thresh, gradient_link_tolerance)
    pts = torch.transpose(pts, 0, 1)
    pgd_bounds = _get_bound_estimation_from_pts(bounded_blocks[1], pts, None, c)
    # NOTE: VERY IMPORTANT CHANGES TO TAPS BOUND TO BE COMPATIBLE WITH CTRAIN WORKFLOW
    pgd_bounds = pgd_bounds[:, 1:]
    pgd_bounds = -pgd_bounds

        
    ibp_lb, ibp_ub = bound_ibp(
        model=bounded_blocks[1],
        ptb=PerturbationLpNorm(x_L=lb, x_U=ub),
        data=data,
        target=target,
        n_classes=n_classes,
    )

    return pgd_bounds, ibp_lb

# TODO: Adapted from TAPS code, should be checked if one wants to use multiestimator PGD loss alone
# TODO: Refactoring needed!!
def _get_pivotal_points(block, input_lb, input_ub, pgd_steps, pgd_restarts, pgd_step_size, pgd_decay_factor, pgd_decay_checkpoints, n_classes, C=None):
    '''
    This assumes the block net is fixed in this procedure. If a BatchNorm is involved, freeze its stat before calling this function.
    '''
    assert C is not None # Should only estimate for the final block
    lb, ub = input_lb.clone().detach(), input_ub.clone().detach()

    pt_list = []
    # split into batches
    # TODO: Can we keep this fixed batch size?
    bs = 128
    lb_batches = [lb[i*bs:(i+1)*bs] for i in range(math.ceil(len(lb) / bs))]
    ub_batches = [ub[i*bs:(i+1)*bs] for i in range(math.ceil(len(ub) / bs))]
    C_batches = [C[i*bs:(i+1)*bs] for i in range(math.ceil(len(C) / bs))]
    for lb_one_batch, ub_one_batch, C_one_batch in zip(lb_batches, ub_batches, C_batches):
        pt_list.append(_get_pivotal_points_one_batch(block, lb_one_batch, ub_one_batch, pgd_steps, pgd_restarts, pgd_step_size, pgd_decay_factor, pgd_decay_checkpoints, n_classes=n_classes, C=C_one_batch))
    pts = torch.cat(pt_list, dim=0)
    return [pts, ]

def _get_pivotal_points_one_batch(block, lb, ub, pgd_steps, pgd_restarts, pgd_step_size, pgd_decay_factor, pgd_decay_checkpoints, C, n_classes, device='cuda'):

    num_pivotal = n_classes - 1 # only need to estimate n_class - 1 dim for the final output

    def init_pts(input_lb, input_ub):
        rand_init = input_lb.unsqueeze(1) + (input_ub-input_lb).unsqueeze(1)*torch.rand(input_lb.shape[0], num_pivotal, *input_lb.shape[1:], device=device)
        return rand_init
    
    def select_schedule(num_steps):
        if num_steps >= 20 and num_steps <= 50:
            lr_decay_milestones = [int(num_steps*0.7)]
        elif num_steps > 50 and num_steps <= 80:
            lr_decay_milestones = [int(num_steps*0.4), int(num_steps*0.7)]
        elif num_steps > 80:
            lr_decay_milestones = [int(num_steps*0.3), int(num_steps*0.6), int(num_steps*0.8)]
        else:
            lr_decay_milestones = []
        return lr_decay_milestones

    lr_decay_milestones = pgd_decay_checkpoints
    lr_decay_factor = pgd_decay_factor
    init_lr = pgd_step_size

    retain_graph = False
    pts = init_pts(lb, ub)
    variety = (ub - lb).unsqueeze(1).detach()
    best_estimation = -1e5*torch.ones(pts.shape[:2], device=pts.device)
    best_pts = torch.zeros_like(pts)
    with torch.enable_grad():
        for re in range(pgd_restarts):
            lr = init_lr
            pts = init_pts(lb, ub)
            for it in range(pgd_steps+1):
                pts.requires_grad = True
                estimated_pseudo_bound = _get_bound_estimation_from_pts(block, pts, None, C=C)
                improve_idx = estimated_pseudo_bound[:, 1:] > best_estimation
                best_estimation[improve_idx] = estimated_pseudo_bound[:, 1:][improve_idx].detach()
                best_pts[improve_idx] = pts[improve_idx].detach()
                # wants to maximize the estimated bound
                if it != pgd_steps:
                    loss = - estimated_pseudo_bound.sum()
                    loss.backward(retain_graph=retain_graph)
                    new_pts = pts - pts.grad.sign() * lr * variety
                    pts = torch.max(torch.min(new_pts, ub.unsqueeze(1)), lb.unsqueeze(1)).detach()
                    if (it+1) in lr_decay_milestones:
                        lr *= lr_decay_factor
    return best_pts.detach()


def _get_bound_estimation_from_pts(block, pts, dim_to_estimate, C=None):
    '''
    only return estimated bounds for dims need to be estimated;
    '''
    if C is None:
        # pts shape (batch_size, num_pivotal, *shape_in[1:])
        out_pts = block(pts.reshape(-1, *pts.shape[2:]))
        out_pts = out_pts.reshape(*pts.shape[:2], -1)
        dim_to_estimate = dim_to_estimate.unsqueeze(1)
        dim_to_estimate = dim_to_estimate.expand(dim_to_estimate.shape[0], out_pts.shape[1], dim_to_estimate.shape[2])
        out_pts = torch.gather(out_pts, dim=2, index=dim_to_estimate) # shape: (batch_size, num_pivotal, num_pivotal)
        estimated_bounds = torch.diagonal(out_pts, dim1=1, dim2=2) # shape: (batch_size, num_pivotal)
    else:
        # # main idea: convert the 9 adv inputs into one batch to compute the bound at the same time; involve many reshaping
        batch_C = C.unsqueeze(1).expand(-1, pts.shape[1], -1, -1).reshape(-1, *(C.shape[1:])) # may need shape adjustment
        batch_pts = pts.reshape(-1, *(pts.shape[2:]))
        out_pts = block(batch_pts)
        out_pts = torch.bmm(batch_C, out_pts.unsqueeze(-1)).squeeze(-1)
        out_pts = out_pts.reshape(*(pts.shape[:2]), *(out_pts.shape[1:]))
        out_pts = - out_pts # the out is the lower bound of yt - yi, transform it to the upper bound of yi - yt
        # the out_pts should be in shape (batch_size, n_class - 1, n_class - 1)
        ub = torch.diagonal(out_pts, dim1=1, dim2=2) # shape: (batch_size, n_class - 1)
        estimated_bounds = torch.cat([torch.zeros(size=(ub.shape[0],1), dtype=ub.dtype, device=ub.device), ub], dim=1) # shape: (batch_size, n_class)

    return estimated_bounds

class RectifiedLinearGradientLink(torch.autograd.Function):
    r'''
    Estabilish Rectified linear gradient link between the input bounds and the input point.
    Note that this is not a valid gradient w.r.t. the forward function
    Take ub as an example: 
        For dims that x[dim] \in [lb, ub-c*(ub-lb)], the gradient w.r.t. ub is 0. 
        For dims that x[dim] == ub, the gradient w.r.t. ub is 1.
        For dims that x[dim] \in [ub-c*(ub-lb), ub], the gradient is linearly interpolated between 0 and 1.
    
    x should be modified to shape (batch_size, *bound_dims) by reshaping.
    bounds should be of shape (1, *bound_dims)
    '''
    @staticmethod
    def forward(ctx, lb, ub, x, c:float, tol:float):
        ctx.save_for_backward(lb, ub, x)
        ctx.c = c
        ctx.tol = tol
        return x
    @staticmethod
    def backward(ctx, grad_x):
        lb, ub, x = ctx.saved_tensors
        c, tol = ctx.c, ctx.tol
        slackness = c * (ub - lb)
        # handle grad w.r.t. ub
        thre = (ub - slackness)
        Rectifiedgrad_mask = (x >= thre)
        grad_ub = (Rectifiedgrad_mask * grad_x * (x - thre).clamp(min=0.5*tol) / slackness.clamp(min=tol)).sum(dim=0, keepdim=True)
        # handle grad w.r.t. lb
        thre = (lb + slackness)
        Rectifiedgrad_mask = (x <= thre)
        grad_lb = (Rectifiedgrad_mask * grad_x * (thre - x).clamp(min=0.5*tol) / slackness.clamp(min=tol)).sum(dim=0, keepdim=True)
        # we don't need grad w.r.t. x and param
        return grad_lb, grad_ub, None, None, None

class GradExpander(torch.autograd.Function):
    '''
    Multiply the gradient by alpha
    '''
    @staticmethod
    def forward(ctx, x, alpha:float=1):
        ctx.alpha = alpha
        return x
    
    @staticmethod
    def backward(ctx, grad_x):
        return ctx.alpha * grad_x, None