import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('baby_img.jpg')
plt.imshow(image),plt.title('Original')
plt.show()


#AVERAGE FILTER

# 5X5 ones matrix and divide them with 25 (5X5)
kernel = np.ones((5,5),np.float32)/25
output1 = cv2.filter2D(image,-1,kernel)
#Apply kernel as filter using Convolution (Convolution is the most important topic in signal processing)

#prevent GUI Crash
cv2.startWindowThread()
#Step 3:- Display an image to the User
cv2.imshow("Averaging",output1)
#Step 4:- Capture anystroke from the user
cv2.waitKey(0)
#Step 5:- Destroy all the previously created instances
cv2.destroyAllWindows()

#average filter without kernal and convolution

blur = cv2.blur(image,(5,5)) #apply simplest average filter (blur filter) using 5X5 kernel matrix
#prevent GUI Crash
cv2.startWindowThread()
#Step 3:- Display an image to the User
cv2.imshow("BLUR",blur)
#Step 4:- Capture anystroke from the user
cv2.waitKey(0)
#Step 5:- Destroy all the previously created instances
cv2.destroyAllWindows()

#Gaussian blurring

#Applying Gaussian Blur Filter for removing Gaussian Noise
gaussianBlur = cv2.GaussianBlur(image,(5,5),0)
#prevent GUI Crash
cv2.startWindowThread()
#Step 3:- Display an image to the User
cv2.imshow("Gaussian Blur",gaussianBlur)
#Step 4:- Capture anystroke from the user
cv2.waitKey(0)
#Step 5:- Destroy all the previously created instances
cv2.destroyAllWindows()

#median blurring

salt_pepper_noised_image = cv2.imread('couple_img.jpg')
median = cv2.medianBlur(salt_pepper_noised_image,5) #Remove salt and pepper noise with median filter


#prevent GUI Crash
cv2.startWindowThread()
#Step 3:- Display an image to the User
cv2.imshow("Noised Image",salt_pepper_noised_image)
cv2.imshow("Median Blur",median)
#Step 4:- Capture anystroke from the user
cv2.waitKey(0)
#Step 5:- Destroy all the previously created instances
cv2.destroyAllWindows()


#bilateral filtering

bilateral = cv2.bilateralFilter(salt_pepper_noised_image,9,75,75) #Bilateral filtering for smoothing and keeping sharp edges

#prevent GUI Crash
cv2.startWindowThread()
#Step 3:- Display an image to the User
cv2.imshow("Median Blur",bilateral)
#Step 4:- Capture anystroke from the user
cv2.waitKey(0)
#Step 5:- Destroy all the previously created instances
cv2.destroyAllWindows()


