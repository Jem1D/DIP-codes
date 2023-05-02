
# import cv2
# import numpy as np

# img=cv2.imread('assets/grey.png',0)
# img = cv2.resize(img,(400,400))
# x,y=img.shape
# z=np.zeros(img.shape,dtype='uint8')

# for i in range (x):
#     for j in range (y):
#         if img[i][j]>=50 and img[i][j]<=150:
#             z[i][j]=255
#         else:
#             z[i][j]=0

# z=np.concatenate((img,z),axis=1)
# # z=np.hstack((img,z))
# cv2.imshow('Without background',z)
# # cv2.imshow('Original image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
import numpy as np

img=cv2.imread('assets/grey.png',0)
img = cv2.resize(img,(400,400))
x,y=img.shape
z=np.zeros(img.shape,dtype='uint8')

for i in range (x):
    for j in range (y):
        if img[i][j]>=50 and img[i][j]<=150:
            z[i][j]=255

        else:
            z[i][j]=img[i][j]

z=np.concatenate((img,z),axis=1)
# z=np.hstack((img,z))
cv2.imshow('With background',z)
# cv2.imshow('Original image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()