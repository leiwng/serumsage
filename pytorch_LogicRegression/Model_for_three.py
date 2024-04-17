# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 20:16:02 2021

@author: GZH
"""

import torch.nn.functional as F
import torch
import torch.nn as nn


class Block(nn.Module):
    '''expand + depthwise + pointwise'''

    def __init__(self, in_planes, out_planes, expansion, stride):
        super(Block, self).__init__()
        self.stride = stride
        planes = expansion * in_planes
        self.conv1 = nn.Conv2d(
            in_planes, planes, kernel_size=1, stride=1, padding=0, bias=False)
        self.bn1 = nn.BatchNorm2d(planes)
        self.conv2 = nn.Conv2d(planes, planes, kernel_size=3,
                               stride=stride, padding=1, groups=planes, bias=False)
        self.bn2 = nn.BatchNorm2d(planes)
        self.conv3 = nn.Conv2d(
            planes, out_planes, kernel_size=1, stride=1, padding=0, bias=False)
        self.bn3 = nn.BatchNorm2d(out_planes)

        self.shortcut = nn.Sequential()
        if stride == 1 and in_planes != out_planes:
            self.shortcut = nn.Sequential(
                nn.Conv2d(in_planes, out_planes, kernel_size=1,
                          stride=1, padding=0, bias=False),
                nn.BatchNorm2d(out_planes),
            )

    def forward(self, x):
        out = F.relu(self.bn1(self.conv1(x)))
        out = F.relu(self.bn2(self.conv2(out)))
        out = self.bn3(self.conv3(out))
        out = out + self.shortcut(x) if self.stride == 1 else out
        return out


class MobileV2(nn.Module):
    def __init__(self):
        super(MobileV2, self).__init__()

        self.backbone = nn.Sequential(
            nn.Conv2d(3, 16, 3, 1, 1),
            nn.ReLU(True),
            nn.MaxPool2d(2, 2),
            Block(16, 32, 3, 1),
            Block(32, 32, 3, 2),
            Block(32, 32, 5, 1),
            Block(32, 32, 5, 2),
            Block(32, 64, 5, 2),
            Block(64, 64, 3, 1),
            Block(64, 32, 3, 2),
            Block(32, 32, 3, 1),
            Block(32, 32, 3, 2),
            Block(32, 16, 3, 1),
            # nn.AvgPool2d(4)
        )
        self.layer1 = nn.Conv2d(3, 16, 3, 1, 1)
        self.layer2 = nn.ReLU(True)
        self.layer3 = nn.MaxPool2d(2, 2)
        self.layer4 = Block(16, 32, 3, 1)
        self.layer5 = Block(32, 32, 3, 2)
        self.layer6 = Block(32, 32, 5, 1)
        self.layer7 = Block(32, 32, 5, 2)
        self.layer8 = Block(32, 64, 5, 2)
        self.layer9 = Block(64, 64, 3, 1)
        self.layer10 = Block(64, 32, 3, 1)
        self.layer11 = Block(32, 32, 3, 1)
        self.layer12 = Block(32, 32, 3, 1)
        self.layer13 = Block(32, 16, 3, 1)

        self.fc = nn.Sequential(
            nn.Linear(16*4*4 + 32*8*8, 64),
            nn.Linear(64, 3))

        self.final_layer = nn.LeakyReLU(0.01, True)
        # self.fc=nn.Linear(16*1*1,3)

    def forward(self, x):

        # y=self.backbone(x)
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
        x = self.layer5(x)

        x = self.layer6(x)
        x = self.layer7(x)
        x_temp = x
        x = self.layer8(x)
        x = self.layer9(x)
        x = self.layer10(x)
        x = self.layer11(x)
        x = self.layer12(x)
        y1 = self.layer13(x)
        y1 = y1.view(-1, 16*y1.shape[2]*y1.shape[3])
        y2 = x_temp.view(-1, 32*x_temp.shape[2]*x_temp.shape[3])

        y = torch.cat([y1, y2], dim=1)
        out = self.fc(y)
        out = torch.exp(out)
        # out = self.final_layer(out)
        return out
