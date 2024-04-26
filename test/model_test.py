import os

from HIL_predictor import HIL_predictor
from utils.chromo_cv_utils import cv_imread
from utils.constants import TUBE_IMG_DIR_FP

predictor = HIL_predictor('./pytorch_yolov5/checkpoints/best.pt','./pytorch_LogicRegression/checkpoints/LHI-model-use.pt')

tube_img_path = TUBE_IMG_DIR_FP

for fn in os.listdir(tube_img_path):
    if fn.endswith('.jpg'):
        img = cv_imread(os.path.join(tube_img_path, fn))
        result = predictor.dealImage(img)
        print(f'{fn}: {result}')

