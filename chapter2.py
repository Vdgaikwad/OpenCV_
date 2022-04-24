import cv2
import numpy as np

img = cv2.imread("Resources/car1.jpg")
kernel = np.ones((2,2),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgBlur1 = cv2.GaussianBlur(img,(7,7),0)
imgCanny = cv2.Canny(img,100,100) #edge detector
#Image dialation = expands the image pixels
imgDialation = cv2.dilate(imgCanny, kernel,iterations=1 )
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Image",img)
cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialate Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)

cv2.waitKey(0)