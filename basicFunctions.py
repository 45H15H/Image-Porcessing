
import cv2

image = cv2.imread("OPENCV/Images/raspberry-pi-400.png")
#cv2.imshow("RPi-400", image)

'''conveting BGR to grayscale'''
# cv2.cvtColor(image to convert, color mode)
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", grayImage)

'''Blur an image, it is used to reduce noise in the photo'''
# Gaussian Blur
# cv2.GaussianBlur(image to blur, kerner size, sigma size( :( idk))
# kerner size is a tuple and is like intensity of the blur
blurImage = cv2.GaussianBlur(image, (7, 7), cv2.BORDER_DEFAULT)
cv2.imshow("Blur Image", blurImage)


'''Edge detection. Using canny which is very popular'''
cannyImage = cv2.Canny(image, 10, 10) # this two values are threshold1 and threshold2
# lower the threshold -> more edges detected
cv2.imshow("Canny edge detection", cannyImage)
# one point to note is that edge detection works great on blured images, so first blur the image then find edges

'''Dilating the image. we use the edge detected image as the structre to dilate'''
dilatedImage = cv2.dilate(cannyImage, (7, 7), iterations=3)
# play with ksize and iterations
cv2.imshow("Dilated Image", dilatedImage)

'''Eroding the image; getting back the structure image from dilated image'''
erodedImage = cv2.erode(dilatedImage, (7, 7), iterations=3)
# passing the same ksize and iterations like that of dilate will kind of give the original edge detected image
cv2.imshow("Eroded Image", erodedImage)


'''Croping: this is done by just slicing of the 3D array'''
croppedImage = image[500:1000, 1000:2000]
cv2.imshow("Cropped image", croppedImage)





cv2.waitKey()