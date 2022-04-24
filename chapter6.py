#joining images

import cv2
import numpy as np
img = cv2.imread("Resources/car1.jpg")



#horizontal stack function
Imghor = np.hstack((img,img))
#vertical stack
ImgVer = np.vstack((img,img))

cv2.imshow("Horizontal", Imghor)
cv2.imshow("vertical", ImgVer)

cv2.waitKey(0)