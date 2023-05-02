import cv2
import numpy as np

img1= cv2.imread('img1.png')
img2= cv2.imread('img2.jpg')

print(img1.shape)

newImg = cv2.resize(img2, (388,581))
img3 = cv2.add(img1,newImg)
# img3 = img1+newImg
cv2.imshow('img',img3)
# cv2.resize()
cv2.waitKey(5000)