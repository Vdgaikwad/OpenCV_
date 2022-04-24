import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

width,height = 250,300
pts1= np.float32([[111,219],[287,188],[158,487],[325,440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("imgOutput",imgOutput)
cv2.waitKey(0)