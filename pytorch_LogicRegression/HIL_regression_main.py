"""
Created on Wed Jun 17 22:12:39 2020

yolov5主程序
@激光码文本检测


@author: GZH
"""


import torch
import numpy as np
import PIL.Image
from pytorch_LogicRegression.Model_for_three import MobileV2
import sys
sys.path.append('./pytorch_LogicRegression')


class HIL_regression(object):
    def __init__(self, regression_model_path):
        self.device = torch.device(
            'cuda:0' if torch.cuda.is_available() else 'cpu')
        self.model = MobileV2()
        self.model.load_state_dict(torch.load(
            regression_model_path, map_location=self.device))
        self.model.eval()

    # 图像预处理函数

        self.mean_rgb = np.array([0.447, 0.407, 0.386])
        self.std_rgb = np.array([0.244, 0.250, 0.253])

    def pad_image(self, image, target_size):
        image = PIL.Image.fromarray(image)

        iw, ih = image.size  # 原始图像的尺寸
        w, h = target_size  # 目标图像的尺寸
        scale = min(w / iw, h / ih)  # 转换的最小比例

        # 保证长或宽，至少一个符合目标图像的尺寸
        nw = int(iw * scale)
        nh = int(ih * scale)

        image = image.resize((nw, nh), PIL.Image.BICUBIC)  # 缩小图像
        # image.show()
        new_image = PIL.Image.new('RGB', target_size, (0, 0, 0))  # 生成灰色图像
        # 计算图像的位置
        # 将图像填充为中间图像，两侧为灰色的样式
        new_image.paste(image, ((w - nw) // 2, (h - nh) // 2))
        # new_image.show()

        return new_image

    def transform(self, img):
        img = img/255.0
        img -= self.mean_rgb
        img /= self.std_rgb
        img = img.transpose(2, 0, 1)  # to verify
        img = torch.from_numpy(img).float()
        img = img.unsqueeze(0)
        return img

    def pre_process(self, img):
        img = self.pad_image(img, (64, 64))
        img = np.array(img, dtype=np.float64)
        img = self.transform(img)
        return img

    def predict(self, imgin):
        # Run inference
        im0 = imgin.copy()
        img = self.pre_process(im0)
        img = img.to(self.device)

        pred = self.model(img).to('cpu')
        pred = pred.detach().numpy()*1000

        return pred
