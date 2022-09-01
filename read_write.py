import os
import cv2
import numpy as np


def imread(path, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
    try:
        img_array = np.fromfile(path, dtype)
        img = cv2.imdecode(img_array, flags)
        return img
    except Exception as e:
        print(e)
        return None


def imwrite(path, img, params=None):
    try:
        extension = os.path.splitext(path)[1]  # 이미지 확장자
        result, encoded_img = cv2.imencode(extension, img, params)

        if result:
            with open(path, mode='w+b') as f:
                encoded_img.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


