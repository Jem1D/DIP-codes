import cv2
import numpy as np

img_noisy1 = cv2.imread('assets/salt_pepper.png',0)
m,n = img_noisy1.shape
img_new1 = np.zeros((m,n), dtype='uint8')

for i in range(1, m-1):
    for j in range(1, n-1):
        temp = [img_noisy1[i-1, j-1],
               img_noisy1[i-1, j],
               img_noisy1[i-1, j + 1],
               img_noisy1[i, j-1],
               img_noisy1[i, j],
               img_noisy1[i, j + 1],
               img_noisy1[i + 1, j-1],
               img_noisy1[i + 1, j],
               img_noisy1[i + 1, j + 1]]
          
        temp = sorted(temp)
        img_new1[i, j]= temp[4]

cv2.imshow('Original',img_noisy1)
cv2.imshow('Blurred',img_new1)



cv2.waitKey(0)
cv2.destroyAllWindows()