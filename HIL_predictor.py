# coding=utf-8
"""The Main Module of HIL indices prediction
"""
__author__ = "王磊"
__copyright__ = "Copyright 2023 四川科莫生医疗科技有限公司"
__credits__ = ["王磊"]
__maintainer__ = "王磊"
__email__ = "lei.wang@kemoshen.com"
__version__ = "0.0.1"
__status__ = "Development"


import os
import time

import cv2
import numpy as np

from pytorch_LogicRegression.HIL_regression_main import HIL_regression
from pytorch_yolov5.yolov5_main import yolov5

from utils.chromo_cv_utils import cv_imread


os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


def get_most_middle_bbox(bboxes):
    """
    get the most middle and big bbox from bboxes
    :param bboxes: [[ymin, xmin, ymax, xmax], [ymin, xmin, ymax, xmax], ...]
    :return: [ymin, xmin, ymax, xmax]
    """
    if len(bboxes) == 1:
        return bboxes[0]

    # 求所有bbox占的矩形区域
    xmin = min(box[1] for box in bboxes)
    xmax = max(box[3] for box in bboxes)
    ymin = min(box[0] for box in bboxes)
    ymax = max(box[2] for box in bboxes)
    # 求所有bbox占的矩形区域的中心点坐标
    center_x = (xmin + xmax) / 2
    center_y = (ymin + ymax) / 2
    # 求距离中心点最近的bbox
    distances = []
    for box in bboxes:
        center_x_temp = (box[1] + box[3]) / 2
        center_y_temp = (box[0] + box[2]) / 2
        distance = (center_x - center_x_temp)**2 + \
            (center_y - center_y_temp)**2
        distances.append(distance)
    index = np.argsort(distances)
    return bboxes[index[0]]


class HIL_predictor(object):
    """HIL indices predictor
    """
    def __init__(self, yolov5_model_path, regression_model_path):
        self.yolov5 = yolov5(yolov5_model_path)
        self.regression = HIL_regression(regression_model_path)

    def dealImage(self, image):
        if (len(image.shape) == 2):
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
        if (image.shape[2] == 1):
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
        bboxes = self.yolov5.detectSiArea(image)
        # return bboxes example:
        # [[array(75, dtype=float32), array(230, dtype=float32), array(102, dtype=float32), array(299, dtype=float32)]]
        # [[ymin, xmin, ymax, xmax]]
        if len(bboxes) == 0:
            # all -1 to indicate no bbox detected
            return {'H': -1, 'I': -1, 'L': -1}

        # 在所有bboxes中取得最中间的bbox
        box_inner = get_most_middle_bbox(bboxes)

        # 对bbox区域进行HIL指数判读
        xmin = max(0, int(box_inner[1]))
        xmax = min(image.shape[0], int(box_inner[3]))
        ymin = max(0, int(box_inner[0]))
        ymax = min(image.shape[1], int(box_inner[2]))
        image_patch = image[xmin:xmax, ymin:ymax]
        # cords_temp = f'{str(ymin)} {str(xmin)} {str(ymax - ymin)} {str(xmax - xmin)}'
        # ymin, xmin, height, width
        box_cords = [ymin, xmin, ymax - ymin, xmax - xmin]

        # 此处调用回归预测算法
        # cv2.namedWindow('aa')
        # cv2.imshow('aa',image_patch)
        # cv2.waitKey(0)
        image_patch = cv2.cvtColor(image_patch, cv2.COLOR_BGR2RGB)
        number_temp = self.regression.predict(image_patch)
        # number_temp:[[10.821  25.049 3.4489]]

        if number_temp.size == 3:

            # L = str(int(np.round(number_temp[0][0])))
            # H = str(int(np.round(number_temp[0][1])))
            # I = str(int(np.round(number_temp[0][2])))
            L = int(np.round(number_temp[0][0]))
            H = int(np.round(number_temp[0][1]))
            I = int(np.round(number_temp[0][2]))

        else:
            # L = str(int(np.round(number_temp[0][0])))
            # all -1 to indicate no number detected
            L = -1
            H = -1
            I = -1

        return {'H': H, 'I': I, 'L': L}


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


if __name__ == '__main__':
    im_fn_list = get_images('./test_images')
    for img_path in im_fn_list:
        image = cv_imread(img_path)
        start = time.time()
        ocr_detector = HIL_predictor(
            './pytorch_yolov5/checkpoints/best.pt', './pytorch_LogicRegression/checkpoints/60000-net3.pt')
        results = ocr_detector.dealImage(image)
        cost_time = time.time()-start
        print("total cost time is: {:.2f}s".format(cost_time))
        print(results)
        for i in range(len(results) // 2):
            box = results[2*i+1]
            cv2.rectangle(image, (int(float(box.split(' ')[0])), int(float(box.split(' ')[1])), int(
                float(box.split(' ')[2])), int(float(box.split(' ')[3]))), (0, 255, 0), 2)
            numbers = results[2*i]
            cv2.putText(image, numbers, (int(float(box.split(' ')[0])), int(
                float(box.split(' ')[1]))), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1)
        cv2.namedWindow('result', cv2.WINDOW_FREERATIO)
        cv2.imshow("result", image)
        cv2.waitKey(0)
    cv2.destroyAllWindows()
