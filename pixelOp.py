import cv2
import numpy as np 
img = cv2.imread("assets/img2.jpg")
img = cv2.resize(img,(400,400))
cv2.imshow("Org", img)
th1,img2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold", img2)
cv2.waitKey(0) 