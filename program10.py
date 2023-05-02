import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("assets/img1.png",0)
M,N = img.shape
H = np.zeros((M,N),dtype=np.float32)
D0 = 50
for u in range(M):
    for v in range(N):
        D = np.sqrt((u-M/2)**2 + (v-N/2)**2)
        if(D <= D0):
            H[u,v] = 1
        else:
            H[u,v] = 0


plt.imshow(H,cmap='gray')
plt.axis('off')
plt.show()

