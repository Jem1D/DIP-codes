import cv2
import numpy as np
# Load image
gray = cv2.imread('assets/lenna.png',0)
gray = cv2.resize(gray,(400,400))

# Roberts Cross Operator
roberts_cross_h = np.array([[1, 0], [0, -1]])
roberts_cross_v = np.array([[0, 1], [-1, 0]])
# Apply Roberts Cross operator horizontally and vertically 
roberts_h = cv2.filter2D(gray, -1, roberts_cross_h)
roberts_v = cv2.filter2D(gray, -1, roberts_cross_v)
# Combine the results
roberts = cv2.addWeighted(roberts_h, 0.5, roberts_v, 0.5, 0)

# Sobel Operator
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
# Combine the results
sobel = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)


cv2.imshow('Original Image', gray)
cv2.imshow('Roberts Cross Operator', roberts)
cv2.imshow('Sobel Operator', sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()