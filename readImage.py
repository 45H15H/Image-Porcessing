
import cv2

# cv2.imread() takes a path to the image and returns matrix of pixels, like we did in Image Processing course
image = cv2.imread("OPENCV/Images/rasp.png")

# To show the image use cv2.imshow(). First parameter is name of the window which shows
# the image and next is the image object itself.
cv2.imshow('Raspberry', image)

# To hold the image
cv2.waitKey(0)