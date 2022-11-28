# _*_ coding: utf-8 _*_
# @Time: 2022/11/22 9:29
# @Auther: 黄家兴
# @File: tupiananhua
# @Project: 王宁

import cv2
import numpy as np
import matplotlib.pyplot as plt


def imgBrightness(img1, c, b):
    rows, cols, channels = img1.shape
    blank = np.zeros([rows, cols, channels], img1.dtype)
    rst = cv2.addWeighted(img1, c, blank, 1 - c, b)
    return rst


img = cv2.imread(r'E:\work\test\raw_pictures\raw1.jpg')
dst = imgBrightness(img, 0.5, 0)
dst2 = imgBrightness(img, 1.5, 0)

cv2.namedWindow("origin", 0)
cv2.resizeWindow("origin", 640, 480)
cv2.imshow('origin', img)


cv2.namedWindow("enhanced", 0);
cv2.resizeWindow("enhanced", 640, 480)
cv2.imshow('enhanced', dst)

cv2.namedWindow("enhanced2", 0);
cv2.resizeWindow("enhanced2", 640, 480)
cv2.imshow('enhanced2', dst2)

cv2.waitKey(0)

#关闭所有窗口
cv2.destroyAllWindows()