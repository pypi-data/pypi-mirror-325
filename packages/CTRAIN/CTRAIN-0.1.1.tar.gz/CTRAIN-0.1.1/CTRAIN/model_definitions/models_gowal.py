import torch
import torch.nn as nn

import numpy as np


class GowalConvSmall(nn.Module):
    def __init__(self, in_shape=(1, 28, 28), n_classes=10, dataset='mnist'):
        super(GowalConvSmall, self).__init__()
        in_channels = in_shape[0]
        if dataset == 'mnist':
            linear_in = 3200
        elif dataset == 'cifar10':
            linear_in = 4608
        self.layers = nn.Sequential(
            nn.Conv2d(in_channels, 16, kernel_size=(4,4), stride=2),
            nn.ReLU(inplace=True),
            nn.Conv2d(16, 32, kernel_size=(4, 4), stride=1),
            nn.ReLU(inplace=True),
            nn.Flatten(),
            nn.Linear(linear_in, 100),
            nn.ReLU(inplace=True),
            nn.Linear(100, 10)
        )
    
    def forward(self, x):
        return self.layers(x)


class GowalConvMed(nn.Module):
    def __init__(self, in_shape=(1, 28, 28), n_classes=10, dataset='mnist'):
        super(GowalConvMed, self).__init__()
        in_channels = in_shape[0]
        if dataset == 'mnist':
            linear_in = 1024
        elif dataset == 'cifar10':
            linear_in = 1600
        self.layers = nn.Sequential(
            nn.Conv2d(in_channels, 32, kernel_size=(3,3), stride=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(32, 32, kernel_size=(4, 4), stride=2),
            nn.ReLU(inplace=True),
            nn.Conv2d(32, 64, kernel_size=(3, 3), stride=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(64, 64, kernel_size=(4, 4), stride=2),
            nn.ReLU(inplace=True),
            nn.Flatten(),
            nn.Linear(linear_in, 512),
            nn.ReLU(inplace=True),
            nn.Linear(512, 512),
            nn.ReLU(inplace=True),
            nn.Linear(512, 10)
        )
    
    def forward(self, x):
        return self.layers(x)

class GowalConvLarge(nn.Module):
    def __init__(self, in_shape=(1, 28, 28), n_classes=10, dataset='mnist'):
        super(GowalConvLarge, self).__init__()
        in_channels = in_shape[0]
        if dataset == 'mnist':
            linear_in = 6272
        elif dataset == 'cifar10':
            linear_in = 10368
        self.layers = nn.Sequential(
            nn.Conv2d(in_channels, 64, kernel_size=(3,3), stride=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(64, 64, kernel_size=(3,3), stride=1), 
            nn.ReLU(inplace=True),
            nn.Conv2d(64, 128, kernel_size=(3,3), stride=2),
            nn.ReLU(inplace=True),
            nn.Conv2d(128, 128, kernel_size=(3,3), stride=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(128, 128, kernel_size=(3,3), stride=1),
            nn.ReLU(inplace=True),
            nn.Flatten(),
            nn.Linear(linear_in, 512),
            nn.ReLU(inplace=True),
            nn.Linear(512, 10)
        )
    
    def forward(self, x):
        return self.layers(x)