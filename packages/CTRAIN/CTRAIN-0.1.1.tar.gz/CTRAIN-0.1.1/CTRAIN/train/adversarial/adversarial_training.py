import torch
import torch.optim as optim
import torch.nn as nn

from art.estimators.classification import PyTorchClassifier
from art.attacks.evasion import ProjectedGradientDescent

from CTRAIN.eval import eval_epoch
from CTRAIN.util import save_checkpoint

def pgd_train_model(hardened_model, train_loader, val_loader=None, num_epochs=100, eps=0.3, input_shape=(1, 28, 28), n_classes=10, learning_rate=0.001,
                    results_path="./results"):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    optimizer=optim.Adam(lr=learning_rate, params=hardened_model.parameters())
    criterion = nn.CrossEntropyLoss()
    classifier = PyTorchClassifier(
        model=hardened_model,
        clip_values=(-0.42421296, 2.82148671),
        input_shape=(1, 28, 28),
        nb_classes=n_classes,
        loss=criterion
    )
    attack = ProjectedGradientDescent(
        estimator=classifier,
        eps=eps,
        eps_step=eps/4.0,
        max_iter=7,
        num_random_init=1,
        verbose=False
    )
    
    for epoch in range(num_epochs):
        hardened_model.train()
        running_loss = 0.0
        for data, target in train_loader:
            data, target = data.to(device), target.to(device)
            adv_samples = attack.generate(data.cpu().numpy())
            adv_samples = torch.from_numpy(adv_samples).to(device)
            optimizer.zero_grad()
            output = hardened_model(adv_samples)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()
            
            running_loss += loss.item()
        
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {running_loss/len(train_loader):.4f}')
        
        correct_clean, correct_adv, total = 0, 0, 0
        for data, target in val_loader:
            data, target = data.to(device), target.to(device)
            output = hardened_model(data)
            predicted = torch.argmax(output, dim=1)
            total += target.size(0)
            correct_clean += torch.sum(predicted == target)
            adv_samples = attack.generate(data.cpu().numpy())
            adv_samples = torch.from_numpy(adv_samples).to(device)
            adv_output = hardened_model(adv_samples)
            adv_predicted = torch.argmax(adv_output, dim=1)
            correct_adv += torch.sum(adv_predicted == target)
            
        print(f"Epoch [{epoch+1}/{num_epochs}], VAL ACC: {correct_clean / total}, ADV. VAL. ACC: {correct_adv / total}")
        eval_epoch(
            model=hardened_model,
            optimizer=optimizer,
            loss=running_loss,
            data_loader=train_loader,
            eps=eps,
            n_classes=n_classes,
            epoch=epoch,
            device=device,
            results_path=f"{results_path}/{epoch}"
        )
        save_checkpoint(hardened_model, optimizer, running_loss, epoch + 1, f"{results_path}/{epoch}")

    return hardened_model

