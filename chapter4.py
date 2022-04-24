import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#print(img)

#add some color
#img[200:300,200:300]= 0,255,0

#create line
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)

#create rectangle
#cv2.FILLED: help to filled the shape
cv2.rectangle(img,(0,0),(255,350),(0,0,255),3)

#to put text
cv2.putText(img,"OpenCV ",(300,300),cv2.FONT_HERSHEY_PLAIN,3,(0,200,200),2)
cv2.circle(img,(400,50),30,(255,255,0),5)
cv2.imshow("Image",img)

cv2.waitKey(0)