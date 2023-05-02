import cv2
import numpy as np

img = cv2.imread('assets/img2.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

img = cv2.resize(img,(400,400))

#Red color rangle  169, 100, 100 , 189, 255, 255


lower_range = np.array([41,70,100])
upper_range = np.array([61,255,255])

mask = cv2.inRange(hsv, lower_range, upper_range)
mask = cv2.resize(mask,(400,400))
cv2.imshow('image', img)
cv2.imshow('mask', mask)


cv2.waitKey(0)
cv2.destroyAllWindows()