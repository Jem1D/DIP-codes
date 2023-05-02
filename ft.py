import numpy as np
import cv2 as cv

a = np.hstack([np.zeros((256,128)), np.ones((256,128))])
af = np.fft.fftshift(np.fft.fft2(a))
afl = abs(af)

print(afl)