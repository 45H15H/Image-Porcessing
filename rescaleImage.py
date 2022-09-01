
import cv2

image = cv2.imread("OPENCV/Images/rasp.png")

print(image.shape) # just like we did in ImageProcssing
# it gives the resolution of the image and the third argument tells that it is 3D array

# rescaling is changing the resolution of the image (automatically changes size also)
small_image = cv2.resize(image, (0, 0), fx = 1.3, fy = 1.3) # fx and fy values are like percent of the image scale to show
# second argument (0, 0) is fixed just change fx and fy
# note that fx and fy has to be same to maintain the aspect ratio of the image

cv2.imshow("Raspberry", small_image)

cv2.waitKey(0)