import cv2
import numpy as np

img1= cv2.imread('assets/img1.png')
# img2 = img1.copy()
# cv2.randn(img2,(0,0,0),(50,50,50))


# img3 = img1+img2
image = []
for i in range(20):
    c = img1.copy()
    cv2.randn(c,(0,0,0),(50,50,50))
    image.append(img1+c)

# removing noise using averaging

img_avg = np.zeros((img1.shape[0],img1.shape[1],img1.shape[2]),np.float32)

for i in image:
    img_avg = img_avg+i/20
    img_avg = np.array(np.round(img_avg),dtype=np.uint8)


cv2.imshow('Original',img1)
#     image.append(c+img1)
cv2.imshow('Resolved',img_avg)
cv2.imshow('Noisy',image[0])
# cv2.resize()
cv2.waitKey(3000)
