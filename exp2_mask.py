import cv2
import numpy as np
img = cv2.imread('assets/img2.jpg')
img = cv2.resize(img,(400,400))

blank = np.zeros(img.shape,dtype='uint8')

circle = cv2.circle(blank,(img.shape[0]//2-35,img.shape[1]//2),120,(255,255,255),-1)
cv2.imshow("CIrcle",circle)

final = cv2.bitwise_and(img,circle)

cv2.imshow("Original",img)
cv2.imshow("Final",final)

cv2.waitKey(0)
cv2.destroyAllWindows()