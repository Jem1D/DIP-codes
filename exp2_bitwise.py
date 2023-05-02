import cv2
import numpy as np

img = cv2.imread('assets/circle.png')
hex = cv2.imread('assets/hex.png')


img = cv2.resize(img,(300,300))
hex = cv2.resize(hex,(300,300))

cv2.imshow('hex',hex)

bit_and = cv2.bitwise_and(img,hex)
bit_xor = cv2.bitwise_xor(img,hex)
bit_or = cv2.bitwise_or(img,hex)
bit_not = cv2.bitwise_not(img,hex)
# bright = cv2.multiply(img, mat)

cv2.imshow('Original',img)
cv2.imshow('AND',bit_and)
cv2.imshow('Or',bit_or)
cv2.imshow('Xor',bit_xor)
cv2.imshow('Not',bit_not)

cv2.waitKey(0)
cv2.destroyAllWindows()