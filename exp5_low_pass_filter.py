import cv2
import numpy as np
img = cv2.imread("assets/img2.jpg",0)
img = cv2.resize(img,(400,400))
kernel_3 = np.ones((5,5),dtype=np.float32)/25

out = cv2.filter2D(img,-1,kernel_3)
out1 = cv2.GaussianBlur(img,(5,5),7)

cv2.imshow('Blur using Filter2D',out)
cv2.imshow("Gaussian",out1)
cv2.imshow("Original Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()