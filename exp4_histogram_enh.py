import cv2
import numpy as np
from matplotlib import pyplot as plt

# for grayscale image

less_con_img = cv2.imread('assets/blur.png',0)
# less_con_img = cv2.cvtColor(less_con_img, cv2.COLOR_BGR2GRAY)
hist1 = cv2.calcHist([less_con_img], [0],None, [256], [0,255])
plt.plot(hist1)

hi_con_img = cv2.equalizeHist(less_con_img)
hist2 = cv2.calcHist([hi_con_img], [0],None, [256], [0,255])
plt.plot(hist2)

cv2.imshow('original',less_con_img)
cv2.imshow('hi contrast', hi_con_img)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()


#for color image

# less_con_img = cv2.imread('assets/blur.png')
# hist1_r = cv2.calcHist([less_con_img], [0],None, [256], [0,256])
# hist1_g = cv2.calcHist([less_con_img], [1],None, [256], [0,256])
# hist1_b = cv2.calcHist([less_con_img], [2],None, [256], [0,256])
# plt.plot(hist1_r)
# plt.plot(hist1_g)
# plt.plot(hist1_b)

# cv2.imshow('original',less_con_img)
# plt.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()