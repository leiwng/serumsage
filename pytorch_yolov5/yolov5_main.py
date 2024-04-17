"""
Created on Wed Jun 17 22:12:39 2020

yolov5主程序
@激光码文本检测


@author: GZH
"""

import numpy as np
import cv2
import torch
from pytorch_yolov5.utils_yolo.utils import *
import sys
sys.path.append('./pytorch_yolov5')


class yolov5(object):
    def __init__(self, yolov5_model_path):
        self.conf_thres = 0.25
        self.iou_thres = 0.45
        self.device = torch.device(
            'cuda:0' if torch.cuda.is_available() else 'cpu')
        self. model = torch.load(
            yolov5_model_path, map_location=self.device)['model']
        self.stride = int(self.model.stride.max())  # model stride
        self.names = self.model.module.names if hasattr(
            self.model, 'module') else self.model.names  # get class names
        self.model.eval()
        # Get names and colors
        self.names = self.model.names if hasattr(
            self.model, 'names') else self.model.modules.names
    # 图像预处理函数

    def letterbox(self, img, new_shape=(640, 640), color=(114, 114, 114), auto=True, scaleFill=False, scaleup=True):
        # Resize image to a 32-pixel-multiple rectangle https://github.com/ultralytics/yolov3/issues/232
        shape = img.shape[:2]  # current shape [height, width]
        if isinstance(new_shape, int):
            new_shape = (new_shape, new_shape)

        # Scale ratio (new / old)
        r = min(new_shape[0] / shape[0], new_shape[1] / shape[1])
        # only scale down, do not scale up (for better test mAP)
        if not scaleup:
            r = min(r, 1.0)

        # Compute padding
        ratio = r, r  # width, height ratios
        new_unpad = int(round(shape[1] * r)), int(round(shape[0] * r))
        dw, dh = new_shape[1] - new_unpad[0], new_shape[0] - \
            new_unpad[1]  # wh padding
        if auto:  # minimum rectangle
            dw, dh = np.mod(dw, 64), np.mod(dh, 64)  # wh padding
        elif scaleFill:  # stretch
            dw, dh = 0.0, 0.0
            new_unpad = new_shape
            ratio = new_shape[0] / shape[1], new_shape[1] / \
                shape[0]  # width, height ratios
        dw /= 2  # divide padding into 2 sides
        dh /= 2
        if shape[::-1] != new_unpad:  # resize
            img = cv2.resize(img, new_unpad, interpolation=cv2.INTER_LINEAR)
        top, bottom = int(round(dh - 0.1)), int(round(dh + 0.1))
        left, right = int(round(dw - 0.1)), int(round(dw + 0.1))
        img = cv2.copyMakeBorder(
            img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)  # add border
        return img, ratio, (dw, dh)

    def detectSiArea(self, imgin):
        result = []
        # 结果返回变量，数据类型：vector<int>
        # 数据顺序： bbox(int:xyxy,用","分割)，只返回文本坐标
        # Run inference
        im0 = imgin.copy()
        img = self.letterbox(imgin, new_shape=[640, 640])[0]
        img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, to 3x416x416
        img = np.ascontiguousarray(img)
        img = torch.from_numpy(img).to(self.device)
        img = img.float()
        img /= 255.0  # 0 - 255 to 0.0 - 1.0
        gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]
        if img.ndimension() == 3:
            img = img.unsqueeze(0)  # 添加batch维度
        with torch.no_grad():
            pred = self.model(img)[0]
        # Apply NMS
        pred = non_max_suppression(pred, self.conf_thres, self.iou_thres)
        # Process detections
        for det in pred:
            if det is not None and len(det):
                det[:, :4] = scale_coords(
                    img.shape[2:], det[:, :4], im0.shape).round()
                result.extend(
                    [
                        xyxy[0].cpu().numpy(),
                        xyxy[1].cpu().numpy(),
                        xyxy[2].cpu().numpy(),
                        xyxy[3].cpu().numpy(),
                    ]
                    for *xyxy, conf, cls in det
                )
        return result
