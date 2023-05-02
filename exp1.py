import cv2
import numpy as np

img = cv2.imread('assets/img2.jpg')
img = cv2.resize(img,(300,400))
mat = np.ones(img.shape, dtype='uint8') * 12

bright = cv2.multiply(img, mat)
divide = cv2.divide(img, mat)
add = cv2.add(img, mat)
light = cv2.subtract(img, mat)

cv2.imshow('Original',img)
cv2.imshow('Multiply',bright)
cv2.imshow('Subtract',light)
cv2.imshow('Divided',divide)
cv2.imshow('Added',add)
# print(mat)

cv2.waitKey(0)
cv2.destroyAllWindows()