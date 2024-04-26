# coding=utf-8
"""The Module of utils functions
"""
__author__ = "王磊"
__copyright__ = "Copyright 2023 四川科莫生医疗科技有限公司"
__credits__ = ["王磊"]
__maintainer__ = "王磊"
__email__ = "lei.wang@kemoshen.com"
__version__ = "0.0.1"
__status__ = "Development"


import os
import hashlib


def md5_of_file(file_path):
    """get md5 hash of a file

    Args:
        file_path (_type_): _description_

    Returns:
        _type_: _description_
    """
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(128 * md5_hash.block_size), b""):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()


def get_files_with_extensions(folder_path, extensions):
    """Get file paths with specific extensions in a folder

    Args:
        folder_path (String): File folder path, e.g. TUBE_IMG_DIR_FP, the folder must be exist
        extensions (List of String): List of File extensions, e.g. ['jpg', 'png', 'jpeg', 'JPG','bmp']

    Returns:
        List of String: List of file paths, e.g. ['./test/tube_img/1.jpg', './test/tube_img/2.jpg']
    """
    files = []
    for fn in os.listdir(folder_path):
        files.extend(os.path.join(folder_path, fn) for ext in extensions if fn.endswith(ext))
    return files


def convert_HIL_indices_to_class(HIL):
    H_ranges = {
        (-2, 0): "", # add this range for handle the case that HIL['H'] is -1 which is for exception case
        (0, 20): "-",
        (20, 50): "+",
        (50, 150): "++",
        (150, 250): "+++",
        (250, float('inf')): "++++"
    }

    I_ranges = {
        (-2, 0): "", # add this range for handle the case that HIL['H'] is -1 which is for exception case
        (0, 10): "-",
        (10, 20): "+",
        (20, 40): "++",
        (40, 50): "+++",
        (50, float('inf')): "++++"
    }

    L_ranges = {
        (-2, 0): "", # add this range for handle the case that HIL['H'] is -1 which is for exception case
        (0, 10): "-",
        (10, 30): "+",
        (30, 50): "++",
        (50, 100): "+++",
        (100, float('inf')): "++++"
    }

    # check H
    for key, H_sqr in H_ranges.items():
        if HIL['H'] >= key[0] and HIL['H'] < key[1]:
            break

    # check I
    for key, I_sqr in I_ranges.items():
        if HIL['I'] >= key[0] and HIL['I'] < key[1]:
            break

    # check L
    for key, L_sqr in L_ranges.items():
        if HIL['L'] >= key[0] and HIL['L'] < key[1]:
            break

    return H_sqr, I_sqr, L_sqr
