from concurrent.futures import ProcessPoolExecutor
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from auto_LiRPA import BoundedModule, PerturbationLpNorm

from CTRAIN.bound.taps import GradExpander
from CTRAIN.eval import eval_acc, eval_certified, eval_epoch
from CTRAIN.bound import bound_ibp
from CTRAIN.train.certified.eps_scheduler import SmoothedScheduler
from CTRAIN.train.certified.losses import get_ibp_loss, get_sabr_loss, get_taps_loss
from CTRAIN.train.certified.initialisation import ibp_init_shi
from CTRAIN.train.certified.regularisers import get_shi_regulariser
from CTRAIN.util import save_checkpoint
from CTRAIN.train.certified.regularisers import get_l1_reg
from CTRAIN.train.certified.certified_training.util import split_network


def taps_train_model(original_model, hardened_model, train_loader, val_loader=None, num_epochs=None, eps=0.3, eps_std=.3, eps_schedule=(0, 20, 50), eps_schedule_unit='epoch', eps_scheduler_args=dict(), optimizer=None,
                    lr_decay_schedule=(15, 25), lr_decay_factor=10, lr_decay_schedule_unit='epoch', 
                    n_classes=10, gradient_clip=None, l1_regularisation_weight=0.00001,
                    shi_regularisation_weight=.5, shi_reg_decay=True, gradient_expansion_alpha=5.,
                    taps_pgd_steps=20, taps_pgd_step_size=None, taps_pgd_restarts=1, 
                    taps_pgd_decay_factor=.2, taps_pgd_decay_checkpoints=(5,7), taps_gradient_link_thresh=.5, taps_gradient_link_tolerance=0.00001,
                    start_epoch=0, results_path="./results", device='cuda'):
    
    criterion = nn.CrossEntropyLoss(reduction='none')
    if start_epoch == 0:
        ibp_init_shi(original_model, hardened_model)

    no_batches = 0
    cur_lr = optimizer.param_groups[-1]['lr']

    # Important Change to Vanilla IBP: Schedule Eps smoothly
    eps_scheduler = SmoothedScheduler(
        num_epochs=num_epochs,
        eps=eps,
        mean=train_loader.mean,
        std=train_loader.std,
        eps_schedule_unit=eps_schedule_unit,
        eps_schedule=eps_schedule,
        batches_per_epoch=len(train_loader),
        start_epoch=start_epoch,
        **eps_scheduler_args
    )


    for epoch in range(num_epochs):
        
        if start_epoch > epoch:
            continue
        
        cur_eps = eps_scheduler.get_cur_eps()
        
        epoch_nat_err = 0
        epoch_rob_err = 0
        
        if lr_decay_schedule_unit == 'epoch':
            if epoch + 1 in lr_decay_schedule:
                print("LEARNING RATE DECAYED!")
                cur_lr = cur_lr * lr_decay_factor
                for g in optimizer.param_groups:
                    g['lr'] = cur_lr

        
        print(f"[{epoch + 1}/{num_epochs}]: eps {[channel_eps for channel_eps in cur_eps]}")
        
        for block in hardened_model.bounded_blocks:
            block.train()

        running_loss = 0.0
        
        for batch_idx, (data, target) in enumerate(train_loader):

            cur_eps = eps_scheduler.get_cur_eps().reshape(-1, 1, 1)
            
            ptb = PerturbationLpNorm(eps=cur_eps, norm=np.inf, x_L=torch.clamp(data - cur_eps, train_loader.min, train_loader.max).to(device), x_U=torch.clamp(data + cur_eps, train_loader.min, train_loader.max).to(device))
              
            if lr_decay_schedule_unit == 'batch':
                if no_batches + 1 in lr_decay_schedule:
                    print("LEARNING RATE DECAYED!")
                    cur_lr = cur_lr * lr_decay_factor
                    for g in optimizer.param_groups:
                        g['lr'] = cur_lr
            
            data, target = data.to(device), target.to(device)
            optimizer.zero_grad()
            clean_output = hardened_model(data)
            regular_err = torch.sum(torch.argmax(clean_output, dim=1) != target).item() / data.size(0)
            epoch_nat_err += regular_err
            clean_loss = criterion(clean_output, target).mean()
            
            
            if eps_scheduler.get_cur_eps(normalise=False) == 0.:
                loss = clean_loss
            elif eps_scheduler.get_cur_eps(normalise=False) != 0. and (eps_scheduler.get_cur_eps(normalise=False) != eps_scheduler.get_max_eps(normalise=False)):
                reg_loss, robust_err = get_ibp_loss(
                    hardened_model=hardened_model,
                    ptb=ptb,
                    data=data,
                    target=target,
                    n_classes=n_classes,
                    criterion=criterion,
                    return_bounds=False,
                    return_stats=True
                )
                
                loss_regularisers = get_shi_regulariser(
                    model=hardened_model,
                    ptb=ptb,
                    data=data,
                    target=target,
                    eps_scheduler=eps_scheduler,
                    n_classes=n_classes,
                    device=device,
                    included_regularisers=['relu', 'tightness'],
                    verbose=False,
                    regularisation_decay=shi_reg_decay
                )
                epoch_rob_err += robust_err
                loss_regularisers = shi_regularisation_weight * loss_regularisers
                loss = reg_loss + loss_regularisers                        
                
            elif (eps_scheduler.get_cur_eps(normalise=False) == eps_scheduler.get_max_eps(normalise=False)):
                loss, robust_err = get_taps_loss(
                    original_model=original_model,
                    hardened_model=hardened_model,
                    bounded_blocks=hardened_model.bounded_blocks,
                    criterion=criterion,
                    data=data,
                    target=target,
                    n_classes=n_classes,
                    ptb=ptb,
                    device=device,
                    pgd_steps=taps_pgd_steps,
                    pgd_restarts=taps_pgd_restarts,
                    pgd_step_size=taps_pgd_step_size,
                    pgd_decay_checkpoints=taps_pgd_decay_checkpoints,
                    pgd_decay_factor=taps_pgd_decay_factor,
                    gradient_link_thresh=taps_gradient_link_thresh,
                    gradient_link_tolerance=taps_gradient_link_tolerance,
                    gradient_expansion_alpha=gradient_expansion_alpha,
                    propagation="IBP",
                    return_stats=True
                )
                
                epoch_rob_err += robust_err
            else:
                assert False, "One option must be true!"
                
            if l1_regularisation_weight is not None:
                l1_regularisation = l1_regularisation_weight * get_l1_reg(model=original_model, device=device)
                loss += l1_regularisation
                
            loss.backward()
            
            if gradient_clip is not None:
                nn.utils.clip_grad_value_(hardened_model.parameters(), clip_value=gradient_clip)
            
            optimizer.step()
            
            running_loss += loss.item()
            eps_scheduler.batch_step()
            no_batches += 1
        
        train_acc_nat = (1 - epoch_nat_err / len(train_loader))
        train_acc_cert = (1 - epoch_rob_err / len(train_loader))

        print(f'Epoch [{epoch+1}/{num_epochs}], Train Loss: {running_loss/len(train_loader):.4f}')
        print(f'\t Natural Acc. Train: {train_acc_nat:.4f}')
        print(f'\t Adv. Acc. Train: N/A')
        print(f'\t Certified Acc. Train: {train_acc_cert:.4f}')

        if results_path is not None:
            save_checkpoint(hardened_model, optimizer, running_loss, epoch + 1, results_path)

    return hardened_model