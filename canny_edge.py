import cv2

img = cv2.imread("assets/img2.jpg") # Read image
img = cv2.resize(img,(400,400))

# Setting parameter values
t_lower = 50 # Lower Threshold
t_upper = 150 # Upper threshold

# Applying the Canny Edge filter
edge = cv2.Canny(img, t_lower, t_upper)

cv2.imshow('original', img)
cv2.imshow('edge', edge)
cv2.waitKey(0)
cv2.destroyAllWindows()
