#! py -3
# -*- coding: utf-8 -*-

import cv2
import numpy
import filters
from scipy import ndimage


img = cv2.imread("screen_shot.png")
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
filter_ = filters.SharpenFilter()
kernel = filter_.kernel
print(kernel)
ker = ndimage.convolve(img, kernel)
blurred = cv2.GaussianBlur(img, (11, 11), 0)
g_hpf = img - blurred
cv2.imshow("find-edges", ker)
cv2.imshow("g_hpf", g_hpf)
cv2.waitKey()
cv2.destroyAllWindows()













