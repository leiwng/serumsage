# coding=utf-8
"""The Main Module of upgrade HIL predictor model and HIL regression model to satisfy latest version of torch
"""
__author__ = "王磊"
__copyright__ = "Copyright 2023 四川科莫生医疗科技有限公司"
__credits__ = ["王磊"]
__maintainer__ = "王磊"
__email__ = "lei.wang@kemoshen.com"
__version__ = "0.0.1"
__status__ = "Development"


import torch

# model = torch.load('./pytorch_yolov5/checkpoints/best.pt')
# torch.save(model, './pytorch_yolov5/checkpoints/best_new.pt')

model = torch.load('./pytorch_LogicRegression/checkpoints/60000-net3.pt')
model = model.state_dict()
# torch.save(model, './pytorch_LogicRegression/checkpoints/60000-net3_new.pt')
