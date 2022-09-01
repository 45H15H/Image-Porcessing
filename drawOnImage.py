
from calendar import c
from typing import Any
import cv2
import numpy as np

image = cv2.imread("OPENCV/Images/rasp.png")

# gettign the actual dimension of the image
x, y, D = image.shape # notice no ()
# x = x size, y = y size, D = 3D means three color channels (RGB)

# creating a blank image to draw the shapes on, with the same dimension as of the original image
blank = np.zeros(image.shape, dtype='uint8')
# uint8 is for datatype of images
# we used .zeros method so that the image would be black
cv2.imshow("Blank image", blank)

# to change the color of the image change the numpy array values
blank[:] = 255, 0, 0 # remember B, G, R from 0 to 255
cv2.imshow("Blue Image", blank)

# we can not only color the whole image, but we can choose the size also like
blank[20:100, 40:100] = 0, 0, 255
# note the x:y x must be smaller than y
cv2.imshow("color box", blank)

# we can draw abstarch simple shapes directly which is used for image processing
cv2.rectangle(blank, (150, 150), (300, 300), (0, 0, 255), 2) # to fill the image set the thickess argument to cv2.FILLED or -1
# arguments are:
#image to draw on, start coordinates, end coordinate, color tuple of BGR, line thickness
cv2.imshow('outline box', blank)

# similarly for circle
cv2.circle(blank, (200, 200), 50, (255, 255, 0), 2)
# argument: on which image to draw, center coordinate, radius, color, line thickness
cv2.imshow('outline circle', blank)


# to draw a single line use cv2.line()
cv2.line(blank, (0, 0), (200, 200), (255, 255, 255), 1)
# arguments are: image on which to draw, start coordinate, end coordinate, color, thickness
cv2.imshow("Line", blank)

# to put text on the image
cv2.putText(blank, 'Hello world', (100, 100), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color = (255, 255, 255))
# arguments are: image on which to text, text to put, coordinates, font style, font scale(size), color
cv2.imshow("text", blank)



#cv2.imshow("raspberry", image)



cv2.waitKey()