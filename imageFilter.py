import cv2
import numpy as np


def binaryImage(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(
        gray, 250, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    return thresh
