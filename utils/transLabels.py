"""Convert Labelme bbox annotations to YOLO style
Example:
    Labelme: 73,227,102,227,73,305,102,305
    YOLO: 1 0.1719056974459725 1.8732394366197183 0.05697445972495088 0.5492957746478874
Explanation:
    Labelme: Left-up-corner-x-coordinate,Left-up-corner-y-coordinate,Right-up-corner-x-coordinate,Right-up-corner-y-coordinate,Left-down-corner-x-coordinate,Left-down-corner-y-coordinate,Right-down-corner-x-coordinate, Right-down-corner-y-coordinate
    YOLO: class_id center_x center_y width height
Convert Algorithm:
    anna_data = '73,227,102,227,73,305,102,305'
    imageSize = [480,640]
    x = float(anna_data.split(',')[0])
    y = float(anna_data.split(',')[1])
    img_width = imageSize[1]
    img_height = imageSize[0]
    width = float(anna_data.split(',')[6])-float(anna_data.split(',')[0])
    height = float(anna_data.split(',')[7])-float(anna_data.split(',')[1])

    center_x = (x + width/2)/img_width
    center_y = (y + height/2)/img_height
    width = width/img_width
    height = height / img_height
    temp = [center_x,center_y,width,height]
"""
__author__ = "王磊"
__copyright__ = "Copyright 2023 四川科莫生医疗科技有限公司"
__credits__ = ["郭正华", "王磊"]
__version__ = "0.0.1"
__maintainer__ = "王磊"
__email__ = "rob@spot.colorado.edu"
__status__ = "Development"


import os
import cv2
from xml.dom.minidom import parse
import xml.dom.minidom
import shutil
def readXML(input_path,imageSize):
    with open(input_path) as f:
        total_anna_data = f.readlines()
    final_bboxes = []# 用于存储所有的bbox
    for anna_data in total_anna_data:

        return _extracted_from_readXML_7(anna_data, imageSize, final_bboxes)


# TODO Rename this here and in `readXML`
def _extracted_from_readXML_7(anna_data, imageSize, final_bboxes):
    x = float(anna_data.split(',')[0])
    y = float(anna_data.split(',')[1])
    img_width = imageSize[1]
    img_height = imageSize[0]
    width = float(anna_data.split(',')[6])-float(anna_data.split(',')[0])
    height = float(anna_data.split(',')[7])-float(anna_data.split(',')[1])

    center_x = (x + width/2)/img_width
    center_y = (y + height/2)/img_height
    width = width/img_width
    height = height / img_height
    temp = [center_x,center_y,width,height]
    final_bboxes.append(temp)
    return final_bboxes

def get_images(input_path):
    files = []
    exts = ['jpg', 'png', 'jpeg', 'JPG','bmp']
    for parent, dirnames, filenames in os.walk(input_path):
        for filename in filenames:
            for ext in exts:
                if filename.endswith(ext):
                    files.append(os.path.join(parent, filename))
                    break
    print(f'Find {len(files)} images')
    return files
def get_annotations(input_path):
    files = []
    exts = ['txt']
    for parent, dirnames, filenames in os.walk(input_path):
        for filename in filenames:
            for ext in exts:
                if filename.endswith(ext):
                    files.append(os.path.join(parent, filename))
                    break
    print(f'Find {len(files)} txt')
    return files

def Write_Text(file_name,text):
    # file_name = 'test.txt'
    with open(file_name,"w") as f:
        f.writelines(text)
        f.writelines("\n")

if __name__ == '__main__':


    folders = [os.getcwd()]

    total_count = 0
    for folder in folders:
        cur_folder = folder
        annotation_folder = f'{cur_folder}/label'
        img_folder = cur_folder + '\imgs'
        annotation_filenames = get_annotations(annotation_folder)
        img_filenames = get_images(img_folder)
        for img_file in img_filenames:
            corr_annotation_filename = (
                f'{annotation_folder}/gt_'
                + img_file.split('\\')[-1][:-4]
                + '.txt'
            )
            if (os.path.exists(corr_annotation_filename)):
                image = cv2.imread(img_file)
                output_img_name = f'G:/Project/yolov5/dataset/labels/train20201013/{str(total_count)}.jpg'
                imageSize = image.shape
                cv2.imwrite(output_img_name,image)
                final_bboxes = readXML(corr_annotation_filename,imageSize)
                # print(final_bboxes)
                for bbox in final_bboxes:
                    str_annotations = '1' + ' ' + str(bbox[0]) + ' ' + str(bbox[1]) + ' ' + str(bbox[2]) + ' ' + str(bbox[3])
                    output_annotation_name = f'G:/Project/yolov5/dataset/labels/train20201013/{str(total_count)}.txt'
                    Write_Text(output_annotation_name,str_annotations)


                total_count = total_count + 1