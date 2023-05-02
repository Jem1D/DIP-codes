# # Question:5 Program for Sharpening an images using high pass filter in frequency domain
# # import libraries
# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
# # Using cv2.imread() method reading an image
# # Using 0 to read image in grayscale mode


# img=cv2.imread('assets/lenna.png',0)
# img = cv2.resize(img,(400,400))
# dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
# dft_shift = np.fft.fftshift(dft)
# magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

# cv2.imshow("Original Image",img)
# cv2.imshow('spectrum',magnitude_spectrum)   

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # plt.subplot(121),plt.imshow(img, cmap = 'gray')
# # plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# # plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
# # plt.title('HPF Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
# # plt.show()


# libraries 
import cv2 
import numpy as np
import matplotlib.pyplot as plt
# original image
f = cv2.imread('assets/lenna.png',0) 
plt.imshow(f, cmap='gray')
plt.axis('off') 
plt.show()
# image in frequency domain 
F = np.fft.fft2(f)
plt.imshow(np.log1p(np.abs(F)),
cmap='gray')
plt.axis('off')
plt.show()
Fshift = np.fft.fftshift(F)
plt.imshow(np.log1p(np.abs(Fshift)),
cmap='gray')
plt.axis('off')
plt.show()
# Filter: High pass 
M,N = f.shape
H = np.zeros((M,N), dtype=np.float32)
D0=50
for u in range(M):
    for v in range(N):
        D = np.sqrt((u-M/2)**2 + (v-N/2)**2)
        if D <= D0:
            H[u,v] = 1
        else:
            H[u,v] = 0
H=1-H
plt.imshow(H, cmap='gray')
plt.axis('off')
plt.show()
# Ideal High Pass Filtering 
Gshift = Fshift * H
plt.imshow(np.log1p(np.abs(Gshift)),
cmap='gray')
plt.axis('off')
plt.show()
# Inverse Fourier Transform 
G = np.fft.ifftshift(Gshift)
plt.imshow(np.log1p(np.abs(G)),
cmap='gray')
plt.axis('off')
plt.show()
# Inverse Fourier Transform
G = np.fft.ifftshift(Gshift) 
plt.imshow(np.log1p(np.abs(G)),
cmap='gray')
plt.axis('off')
plt.show()
g = np.abs(np.fft.ifft2(G)) 
plt.imshow(g, cmap='gray')
plt.axis('off') 
plt.show()
plt.imshow(f, cmap='gray')
plt.axis('off')
plt.show()
