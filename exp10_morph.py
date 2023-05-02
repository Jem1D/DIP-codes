#Import Libraries
import cv2
import numpy as np

img = cv2.imread('assets/bug1.png',0)
img = cv2.resize(img,(400,400))
img = cv2.bitwise_not(img)
cv2.imshow('Original',img)

#define the kernal
kernal = np.ones((3,3),np.uint8)

#erosion of the image ie.removes pixels on object boundaries 
erosion = cv2.erode(img,kernal,iterations = 9)
cv2.imshow('erosion method',erosion)

#Dilation adds pixels to the boundaries of objects in an image
dilation = cv2.dilate(img,kernal,iterations = 9)
cv2.imshow('Dilation',dilation)




opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernal,iterations = 9)
cv2.imshow('Opening',opening)

#The closing operation dilates an image and then erodes the dilated image 
closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernal,iterations = 9)
cv2.imshow('Closing',closing)





cv2.waitKey(0)
cv2.destroyAllWindows()