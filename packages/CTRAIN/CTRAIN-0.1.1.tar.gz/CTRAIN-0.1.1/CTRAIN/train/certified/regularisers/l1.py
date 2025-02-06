import torch
import torch.nn as nn


def get_l1_reg(model, device='cuda'):
    loss = torch.zeros(()).to(device)
    # only regularise Linear and Convolutional layers
    for module in model.modules():
        if isinstance(module, nn.Linear):
            loss += torch.abs(module.weight).sum()
        elif isinstance(module, nn.Conv2d):
            loss += torch.abs(module.weight).sum()
    return loss