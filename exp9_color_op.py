import cv2
import numpy as np
#In open cv we have BGR not RGB
#so first we need to load the image and after that we convert the BGR 
# colour image to HSV color.
img = cv2.imread('assets/colors.png')
img = cv2.resize(img,(450,400))
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#After that you need to determine the lower and upper range for your colors you 
# can use imutils for this propose. basically in the above image we are going to 
# Detect the three blue colors.
lower_range = np.array([110,50,50])
upper_range = np.array([130,255,255])
#After that we need to create the mask of our image.
mask = cv2.inRange(hsv, lower_range, upper_range)
#And at the end we need to show the image and mask.
cv2.imshow('image', img)
cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

