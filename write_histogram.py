# -*- coding: utf-8 -*-
"""
    author : Yoo, JunSang
    date : 2022-09-01
    Save histogram of image directory with Excel file format
"""
from __future__ import print_function
import os
import glob
import cv2
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from read_write import imread

INPUT_DIRECTORY = r'D:\dataset\#02_기준노면(픽셀Resize_1mm_pixel)\아스팔트포장'
WRITE_DIRECTORY = r'D:\dataset\#02_기준노면(픽셀Resize_1mm_pixel)\아스팔트포장.xlsx'
DATA_HEADER = ['name', 'max', 'mean', 'std']


def write_excel(data: list = None, write_path: str = None):
    """
    Save the Excel file
    :param data: Excel data list format 'DATA_HEADER'
    :param write_path: Saving Excel path
    :return: bool
    """
    df = pd.DataFrame(data=data)
    df.columns = DATA_HEADER
    df.to_excel(write_path, float_format='%.2f', index=False)

    return True


def draw_hist(input_path: str = None):
    """
    Draw histogram to find contrast ratio
    :param input_path: Image directory for draw histogram
    :return: List, containing histogram numpy array as elements
    """
    image_paths: list = glob.glob(input_path + '\*.jpg') or \
                        glob.glob(input_path + '\*.bmp') or \
                        glob.glob(input_path + '\*.png')
    data = list()

    if len(image_paths) == 0:
        return print("There is no image files")

    index = 0
    for img_path in image_paths:
        print(fr"Find histogram... [{index + 1} / {len(image_paths)}]", end='\r')
        img_name = os.path.basename(img_path).split('.')[0]
        img = imread(img_path, 0)
        if img is None:
            print(fr"{img_path} is wrong image")
            continue
        hist = cv2.calcHist([img], [0], None, [256], [0, 256])

        data.append([img_name,
                     np.where(hist == np.max(hist))[0][0],
                     np.mean(img),
                     np.std(img)])
        index += 1

    return data


if __name__ == '__main__':
    excel_data = draw_hist(INPUT_DIRECTORY)
    if write_excel(excel_data, WRITE_DIRECTORY):
        print("Success")
