import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from auto_LiRPA import BoundedModule, PerturbationLpNorm

from CTRAIN.eval import eval_acc, eval_certified, eval_epoch
from CTRAIN.train.certified.eps_scheduler import LinearScheduler
from CTRAIN.train.certified.losses import get_ibp_loss
from CTRAIN.util import save_checkpoint
from CTRAIN.train.certified.regularisers import get_l1_reg

def ibp_train_model(original_model, train_loader, val_loader=None, num_epochs=None, eps=0.3, eps_std=.3, eps_schedule=(0, 20, 50), eps_schedule_unit='epoch',
                    learning_rate=0.001, lr_decay_schedule=(15, 25), lr_decay_factor=10, lr_decay_schedule_unit='epoch', 
                    input_shape=(1, 28, 28), n_classes=10, gradient_clip=None, l1_regularisation_weight=0.00001, results_path="./results"):
    
    device = torch.device("cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu")
    image = torch.zeros((1, *input_shape))
    hardened_model = BoundedModule(original_model, image, device=device, bound_opts={"conv_mode": "patches"})
    criterion = nn.CrossEntropyLoss(reduction='none')
    optimizer = optim.Adam(hardened_model.parameters(), lr=learning_rate)

    
    no_batches = 0
    cur_lr = learning_rate
    
    eps_scheduler = LinearScheduler(
        num_epochs=num_epochs,
        eps=eps,
        mean=train_loader.mean,
        std=train_loader.std,
        start_eps=0,
        start_kappa=1,
        end_kappa=0,
        eps_schedule_unit=eps_schedule_unit,
        eps_schedule=eps_schedule,
        batches_per_epoch=len(train_loader)
    )
    
    cur_eps, kappa = eps_scheduler.get_cur_eps(), eps_scheduler.get_cur_kappa()

    # Training loop
    for epoch in range(num_epochs):
        
        if lr_decay_schedule_unit == 'epoch':
            if epoch + 1 in lr_decay_schedule:
                print("LEARNING RATE DECAYED!")
                cur_lr = cur_lr * lr_decay_factor
                for g in optimizer.param_groups:
                    g['lr'] = cur_lr

        
        print(f"[{epoch + 1}/{num_epochs}]: eps {[channel_eps for channel_eps in cur_eps]}, kappa {kappa:.2f} ")
        hardened_model.train()
        running_loss = 0.0
        
        for batch_idx, (data, target) in enumerate(train_loader):

            cur_eps = eps_scheduler.get_cur_eps().reshape(-1, 1, 1)
            kappa = eps_scheduler.get_cur_kappa()
            
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
            
            if eps_scheduler.get_cur_eps(normalise=False) != 0.:
                certified_loss = get_ibp_loss(
                    hardened_model=hardened_model,
                    ptb=ptb,
                    data=data,
                    target=target,
                    n_classes=n_classes,
                    criterion=criterion,
                )
    
                loss = kappa * clean_loss + (1-kappa) * certified_loss
            else:
                loss = clean_loss
            
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
        
        val_acc = "NO VAL PROVIDED"
        if val_loader:
            val_acc, val_acc_cert, val_acc_adv = eval_epoch(
                model=hardened_model,
                data_loader=val_loader,
                eps=cur_eps,
                n_classes=n_classes,
                device=device,
                results_path=f"{results_path}/{epoch}/val",
                test_samples=1000,
                verification_method='IBP'   
            )
        
        train_acc, train_acc_cert, train_acc_adv = eval_epoch(
            model=hardened_model,
            data_loader=train_loader,
            eps=cur_eps,
            n_classes=n_classes,
            device=device,
            results_path=f"{results_path}/{epoch}",
            test_samples=1000,
            verification_method='IBP'
        )

        print(f'Epoch [{epoch+1}/{num_epochs}], Train Loss: {running_loss/len(train_loader):.4f}')
        print(f'\t Natural Acc. Train: {train_acc:.4f}')
        print(f'\t Adv. Acc. Train: {train_acc_adv:.4f}')
        print(f'\t Certified Acc. Train: {train_acc_cert:.4f}')
        if val_loader:
            print(f'\t Natural Acc. Validation: {val_acc:.4f}')
            print(f'\t Adv. Acc. Validation: {val_acc_adv:.4f}')
            print(f'\t Certified Acc. Validation: {val_acc_cert:.4f}')
        save_checkpoint(hardened_model, optimizer, running_loss, epoch + 1, f"{results_path}/{epoch}")


    return hardened_model
