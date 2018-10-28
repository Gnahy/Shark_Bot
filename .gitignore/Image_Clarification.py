# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 01:21:35 2018

@author: Gnahy
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img1.jpg',1)


img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

# equalize the histogram of the Y channel
img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

# convert the YUV image back to RGB format
img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

cv2.imshow('Color input image', img)
cv2.imshow('Histogram equalized', img_output)

cv2.waitKey(0)

""" Clarify Greyscale images
plt.hist(img.ravel(),256,[0,256]); plt.show()

equ = cv2.equalizeHist(img)
plt.hist(equ.ravel(),256,[0,256]); plt.show()

res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imwrite('res.png',res)"""
