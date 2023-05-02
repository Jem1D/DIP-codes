# Python programs to find
# unique HSV code for color

# Importing the libraries openCV & numpy
import cv2
import numpy as np

# Get green color
color = np.uint8([[[255, 255, 0]]])

# Convert Green color to Green HSV
hsv_green = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

# Print HSV Value for Green color
print(hsv_green)

# Make python sleep for unlimited time
cv2.waitKey(0)
