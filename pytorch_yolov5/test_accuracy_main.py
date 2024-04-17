# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 10:28:29 2020

@author: GZH
"""

import argparse

from utils_yolo.datasets import *
from utils_yolo.utils import *
import cv2


def compute_IOU(rec1, rec2):
    """
    计算两个矩形框的交并比。
    :param rec1: (x0,y0,x1,y1)      (x0,y0)代表矩形左上的顶点，（x1,y1）代表矩形右下的顶点。下同。
    :param rec2: (x0,y0,x1,y1)
    :return: 交并比IOU.
    """
    left_column_max = max(rec1[0], rec2[0])
    right_column_min = min(rec1[2], rec2[2])
    up_row_max = max(rec1[1], rec2[1])
    down_row_min = min(rec1[3], rec2[3])
    # 两矩形无相交区域的情况
    if left_column_max >= right_column_min or down_row_min <= up_row_max:
        return 0
    # 两矩形有相交区域的情况
    else:
        S1 = (rec1[2]-rec1[0])*(rec1[3]-rec1[1])
    S2 = (rec2[2]-rec2[0])*(rec2[3]-rec2[1])
    S_cross = (down_row_min-up_row_max)*(right_column_min-left_column_max)
    return S_cross/(S1+S2-S_cross)


def get_image_names(img_root):
    total_file_names = []
    for filepath, dirnames, filenames in os.walk(img_root):
        total_file_names.extend(
            temp_name for temp_name in filenames if temp_name.endswith('.jpg')
        )


device = 'cpu'
model_path = './weights/best.pt'
model = torch.load(model_path, map_location=device)['model']
model = torch.load(weights, map_location=device)['model']
model.to(device).eval()
img_names = get_image_names('./data_for_accuracy_test/20210527/imgs')

for img_name in img_names:
    label_file_name = './data_for_accuracy_test/20210527/labels/' + \
        img_name.replacewith('.jpg', '.txt')
    with open(label_file_name) as f:
        gt_bbox = f.readline()[0]
    img = cv2.imread(img_name)
    img = torch.from_numpy(img).to(device)
    img = img.half() if half else img.float()  # uint8 to fp16/32
    img /= 255.0  # 0 - 255 to 0.0 - 1.0
    if img.ndimension() == 3:
        img = img.unsqueeze(0)

    # Inference
    pred = model(img, augment=opt.augment)[0]

    # Apply NMS
    pred = non_max_suppression(pred, 0.4, 0.5, fast=True)
    for i, det in enumerate(pred):  # detections per image

        if det is not None and len(det):
            # Rescale boxes from img_size to im0 size
            det[:, :4] = scale_coords(
                img.shape[2:], det[:, :4], im0.shape).round()
            for *xyxy, conf, cls in det:
                xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) /
                        gn).view(-1).tolist()  # normalized xywh
