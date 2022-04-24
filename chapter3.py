import cv2


img = cv2.imread("Resources/car1.jpg",1)
print(img.shape)

#to resized the image
imgResize = cv2.resize(img,(1080, 440))

#to crop the image
imgCropped = img[0:600,0:1200] #using matrix
cv2.imshow("Output",img)
cv2.imshow("Output",imgResize)
cv2.imshow("imgCropped ",imgCropped )
cv2.waitKey(0)