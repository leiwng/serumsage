# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 15:24:57 2020

@author: GZH
"""

import os
import cv2
import time
import numpy as np
import matplotlib.pyplot as plt
from utils_yolo.datasets import *
from utils_yolo.utils import *


def get_images(test_data_path):
    files = []
    exts = ['jpg', 'png', 'jpeg', 'JPG', 'bmp']
    for parent, _, filenames in os.walk(test_data_path):
        for filename in filenames:
            for ext in exts:
                if filename.endswith(ext):
                    files.append(os.path.join(parent, filename))
                    break
    print(f'Find {len(files)} images')
    return files


class yolov5(object):
    def __init__(self, model_path, half=True):
        self.device = torch.device(
            'cuda:0' if torch.cuda.is_available() else 'cpu')
        if model_path is not None:
            self.model = torch.load(
                model_path, map_location=self.device)['model']
            self.model.to(self.device)
            self.model.eval()
        else:
            print('no model_path')
        self.half = half
        if half:
            self.model.half()    # to FP16

        img = torch.zeros((1, 3, 160, 160), device=self.device)  # init img
        _ = self.model(
            img.half() if half else img) if self.device.type != 'cpu' else None  # run once
        # Get names and colors
        self.names = self.model.names if hasattr(
            self.model, 'names') else self.model.modules.names
        self.colors = [[random.randint(0, 255) for _ in range(3)]
                       for _ in range(len(self.names))]
        self.conf_thres = 0.4
        self.iou_thres = 0.5
        self.classes = None
        self.agnostic_nms = False

    def detect(self, imageIn, imagePath):
        img = torch.from_numpy(imageIn).to(self.device)
        img = img.half() if self.half else img.float()  # uint8 to fp16/32
        img /= 255.0  # 0 - 255 to 0.0 - 1.0
        if img.ndimension() == 3:
            img = img.unsqueeze(0)  # 添加batch维度，满足torch基本格式
        # inference
        img = img.permute(0, 3, 1, 2)
        # print(img.shape)

        pred = self.model(img)[0]
        pred = non_max_suppression(pred, self.conf_thres, self.iou_thres,
                                   fast=True, classes=self.classes, agnostic=self.agnostic_nms)

        # Process detecti
        s = ''
        save_img = True
        for det in pred:
            if det is not None and len(det):
                # Print results
                for c in det[:, -1].unique():
                    n = (det[:, -1] == c).sum()  # detections per class
                    s += '%g %ss, ' % (n, self.names[int(c)])  # add to string

                for *xyxy, conf, cls in det:
                    label = '%s %.2f' % (self.names[int(cls)], conf)
                    plot_one_box(xyxy, imageIn, label=label,
                                 color=self.colors[int(cls)], line_thickness=3)

        if save_img:
            # Save results (image with detections)
            save_path = './test_dataset/output_video1/' + imagePath.split('\\')[-1]
            cv2.imwrite(save_path, imageIn)


if __name__ == '__main__':

    model_path = './weights/yolov5s.pt'
    yolov5_detector = yolov5(model_path)

    # im_fn_list = get_images('./inference/images')

    # for img_path in im_fn_list:
    #     image = cv2.imread(img_path)
    #     optimal_img_width = check_img_size(image.shape[0])
    #     optimal_img_height = check_img_size(image.shape[1])
    #     resized_image = cv2.resize(image,(optimal_img_height,optimal_img_width))
    #     with torch.no_grad():
    #         start = time.time()
    #         results = yolov5_detector.detect(resized_image,img_path)
    #         cost_time = (time.time() - start)
    #         print(" cost time: {:.2f}s".format(cost_time))

    cap = cv2.VideoCapture('./test_dataset/video20200919/1.mp4')

    nCount = 1
    while (cap.isOpened()):
        img_path = f'{str(nCount)}.jpg'
        ret, image = cap.read()
        optimal_img_width = check_img_size(image.shape[0])
        optimal_img_height = check_img_size(image.shape[1])
        resized_image = cv2.resize(
            image, (optimal_img_height, optimal_img_width))
        with torch.no_grad():
            start = time.time()
            results = yolov5_detector.detect(image, img_path)
            cost_time = (time.time() - start)
            print(" cost time: {:.2f}s".format(cost_time))
        nCount += 1
