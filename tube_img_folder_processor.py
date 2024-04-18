# -*- coding: utf-8 -*-
"""The Module of Tube Image folder process
以独立线程的方式处理试管图片文件夹中的图像文件
- 读取图像文件
- 判定HIL指数

Usage:
    - 在用户的Windows主机上运行该模块
    - 输入用户名称

Author: Lei Wang
Date: April 10, 2024
"""

__author__ = "王磊"
__copyright__ = "Copyright 2023 四川科莫生医疗科技有限公司"
__credits__ = ["王磊"]
__maintainer__ = "王磊"
__email__ = "lei.wang@kemoshen.com"
__version__ = "0.0.1"
__status__ = "Development"


import os
from shutil import move
from datetime import datetime

from PyQt5.QtCore import pyqtSignal, QThread

from utils.utils import (
    get_files_with_extensions,
    convert_HIL_indices_to_class,
    md5_of_file,
)
from utils.chromo_cv_utils import cv_imread



def write_HIL_to_file(HIL, H_sqr, I_sqr, L_sqr, img_fp):
    """将HIL指数写入文件

    Args:
        HIL (Dict): 保存HIL指数的字典
        H_sqr (String): _description_
        I_sqr (_type_): _description_
        L_sqr (_type_): _description_
        img_fp (_type_): _description_
    """
    img_fn = os.path.splitext(os.path.basename(img_fp))[0]
    text_fp = f'{os.path.splitext(img_fp)[0]}.txt'
    with open(text_fp, 'w', encoding='utf-8') as f:
        f.write(f'img_name:{img_fn}' + '\n')
        f.write(f'5078:{H_sqr}' + '\n')
        f.write(f'5079:{I_sqr}' + '\n')
        f.write(f'5080:{L_sqr}' + '\n')
        f.write(f'H:{HIL["H"]}' + '\n')
        f.write(f'I:{HIL["I"]}' + '\n')
        f.write(f'L:{HIL["L"]}' + '\n')
    return text_fp


class TubeImgFolderProcessor(QThread):

    # image path, HIL indices and HIL classes
    imgProcessed = pyqtSignal(str, int, int, int, str, str, str)
    allImgProcessed = pyqtSignal()

    def __init__(self, HIL_predictor, img_folder_fp, img_exts, output_folder_fp):
        super().__init__()
        # input: 1)image folder full path; 2)allowed image extension list 3)HIL indices
        self.img_folder_fp = img_folder_fp
        self.img_exts = img_exts
        self.HIL_predictor = HIL_predictor
        self.output_folder_fp = output_folder_fp

    def run(self):
        # 获取目录下所有图片文件的访问路径
        img_fps = get_files_with_extensions(
            self.img_folder_fp, self.img_exts)
        # 遍历所有图片文件进行处理
        for img_fp in img_fps:
            img = cv_imread(img_fp)
            HIL = self.HIL_predictor.dealImage(img)
            # print(HIL)
            H_sqr, I_sqr, L_sqr = convert_HIL_indices_to_class(HIL)
            img_basename = os.path.basename(img_fp)
            img_fn = os.path.splitext(img_basename)[0]
            img_ext = os.path.splitext(img_basename)[1]

            img_fp_in_dst_folder = os.path.join(
                self.output_folder_fp, img_basename)
            if os.path.exists(img_fp_in_dst_folder):
                cur_dt = datetime.now()
                cur_dt_str = cur_dt.strftime("%Y%m%d%H%M%S%f")[:-3]
                # 避免在已经加上时间戳的文件名再次加时间戳
                # 判断文件名是否已经加上时间戳,比如:_20231025141526125
                if len(img_fn) > len('_20231025141526125') and img_fn[-18] == '_' and img_fn[-17:].isdigit():
                    img_fp_in_dst_folder = os.path.join(
                        self.output_folder_fp, f'{img_fn[:-18]}_{cur_dt_str}{img_ext}')
                else:
                    img_fp_in_dst_folder = os.path.join(
                        self.output_folder_fp, f'{img_fn}_{cur_dt_str}{img_ext}')
            move(img_fp, img_fp_in_dst_folder)
            HIL_fp = write_HIL_to_file(HIL, H_sqr, I_sqr, L_sqr, img_fp_in_dst_folder)

            # 计算MD5
            # Image的MD5
            img_md5_hash = md5_of_file(img_fp_in_dst_folder)
            # HIL的MD5
            HIL_md5_hash = md5_of_file(HIL_fp)
            # 保存MD5
            md5_fp = f'{os.path.splitext(img_fp_in_dst_folder)[0]}.md5'
            with open(md5_fp, 'w', encoding='utf-8') as f:
                f.write(f'img_md5:{img_md5_hash}' + '\n')
                f.write(f'HIL_md5:{HIL_md5_hash}' + '\n')

            self.imgProcessed.emit(os.path.join(
                self.output_folder_fp, img_basename), HIL['H'], HIL['I'], HIL['L'], H_sqr, I_sqr, L_sqr)
        self.allImgProcessed.emit()
