import cv2
import numpy as np

#read image in grayscale mode,because medianBlur not working with RGB images
image = cv2.imread('baby_img.jpg',1)
image_8bit = cv2.imread('baby_img.jpg',0) #Hough transform processing wants 8-bit image


circles = cv2.HoughCircles(image_8bit,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(image,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(image,(i[0],i[1]),2,(0,0,255),3)

cv2.startWindowThread()
cv2.imshow('detected circles',image)
cv2.waitKey(0)
cv2.destroyAllWindows()



