from concurrent.futures import ProcessPoolExecutor
import torch
import torch.nn as nn
import numpy as np
from auto_LiRPA import BoundedModule, PerturbationLpNorm

from CTRAIN.train.certified.eps_scheduler import SmoothedScheduler
from CTRAIN.train.certified.losses import get_mtl_ibp_loss
from CTRAIN.train.certified.initialisation import ibp_init_shi
from CTRAIN.train.certified.regularisers import get_shi_regulariser
from CTRAIN.util import save_checkpoint
from CTRAIN.train.certified.regularisers import get_l1_reg

def mtl_ibp_train_model(original_model, hardened_model, train_loader, val_loader=None, num_epochs=None, eps=0.3, eps_std=0.3, eps_schedule=(0, 20, 50), eps_schedule_unit='epoch', eps_scheduler_args=dict(), optimizer=None,
                        lr_decay_schedule=(15, 25), lr_decay_factor=10, lr_decay_schedule_unit='epoch', 
                        n_classes=10, gradient_clip=None, shi_regularisation_weight=.5, shi_reg_decay=True, l1_regularisation_weight=0.00001, 
                        alpha=.5, pgd_restarts=1, pgd_step_size=10, pgd_n_steps=1, pgd_eps_factor=1, pgd_decay_factor=.1, pgd_decay_checkpoints=(), pgd_early_stopping=False, results_path="./results", device='cuda'):

    criterion = nn.CrossEntropyLoss(reduction='none')

    ibp_init_shi(original_model, hardened_model)

    no_batches = 0
    cur_lr = optimizer.param_groups[-1]['lr']

    eps_scheduler = SmoothedScheduler(
        num_epochs=num_epochs,
        eps=eps,
        mean=train_loader.mean,
        std=train_loader.std,
        eps_schedule_unit=eps_schedule_unit,
        eps_schedule=eps_schedule,
        batches_per_epoch=len(train_loader),
        **eps_scheduler_args
    )

    cur_eps = eps_scheduler.get_cur_eps()

    for epoch in range(num_epochs):
        
        epoch_adv_err = 0
        epoch_rob_err = 0
        epoch_nat_err = 0
        
        if lr_decay_schedule_unit == 'epoch':
            if epoch + 1 in lr_decay_schedule:
                print("LEARNING RATE DECAYED!")
                cur_lr = cur_lr * lr_decay_factor
                for g in optimizer.param_groups:
                    g['lr'] = cur_lr

        
        print(f"[{epoch + 1}/{num_epochs}]: eps {[channel_eps for channel_eps in cur_eps]}")
        hardened_model.train()
        original_model.train()
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
            clean_loss = criterion(clean_output, target).mean()
            regular_err = torch.sum(torch.argmax(clean_output, dim=1) != target).item() / data.size(0)
            epoch_nat_err += regular_err
            
            if eps_scheduler.get_cur_eps(normalise=False) != 0.:
                
                if pgd_eps_factor == 1:
                    pgd_ptb = ptb
                else:
                    pgd_eps = (eps_std * pgd_eps_factor).to(device)
                    data_min, data_max = train_loader.min.to(device), train_loader.max.to(device)
                    pgd_ptb = PerturbationLpNorm(eps=pgd_eps, norm=np.inf, x_L=torch.clamp(data - pgd_eps, data_min, data_max).to(device), x_U=torch.clamp(data + pgd_eps, data_min, data_max).to(device))
                
                loss, robust_err, adv_err = get_mtl_ibp_loss(
                    hardened_model=hardened_model,
                    original_model=original_model,
                    ptb=ptb,
                    data=data,
                    target=target,
                    n_classes=n_classes,
                    criterion=criterion,
                    alpha=alpha,
                    return_bounds=False,
                    return_stats=True,
                    restarts=pgd_restarts,
                    step_size=pgd_step_size,
                    n_steps=pgd_n_steps,
                    pgd_ptb=pgd_ptb,
                    early_stopping=pgd_early_stopping,
                    decay_checkpoints=pgd_decay_checkpoints,
                    decay_factor=pgd_decay_factor,
                    device=device
                )
                epoch_adv_err += adv_err
                epoch_rob_err += robust_err

                                    
            else:
                loss = clean_loss
                
            if (eps_scheduler.get_cur_eps(normalise=False) != eps_scheduler.get_max_eps(normalise=False)):
                # Important Change to Vanilla IBP: Regularise Unstable ReLUs and Bound Tightness during Warm Up/Ramp Up
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
                
                loss_regularisers = (shi_regularisation_weight * loss_regularisers).to(device)
                loss = loss + loss_regularisers
            
            if l1_regularisation_weight is not None:
                l1_regularisation = l1_regularisation_weight * get_l1_reg(model=original_model, device=device)
                loss = loss + l1_regularisation
            
            loss.backward()
            if gradient_clip is not None:
                nn.utils.clip_grad_value_(hardened_model.parameters(), clip_value=gradient_clip)
            optimizer.step()
            
            running_loss += loss.item()
            eps_scheduler.batch_step()
            no_batches += 1

        train_acc_nat = (1 - epoch_nat_err / len(train_loader))
        train_acc_adv = (1 - epoch_adv_err / len(train_loader))
        train_acc_cert = (1 - epoch_rob_err / len(train_loader))

        print(f'Epoch [{epoch+1}/{num_epochs}], Train Loss: {running_loss/len(train_loader):.4f}')
        print(f'\t Natural Acc. Train: {train_acc_nat:.4f}')
        print(f'\t Adv. Acc. Train: {train_acc_adv:.4f}')
        print(f'\t Certified Acc. Train: {train_acc_cert:.4f}')

        if results_path is not None:
            save_checkpoint(hardened_model, optimizer, running_loss, epoch + 1, results_path)

    return hardened_model
