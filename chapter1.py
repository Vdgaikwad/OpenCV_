import cv2
# print("Package Imaported")


'''
#To read the image
img = cv2.imread("Resources/Morepankh.jpg")

#Image show
cv2.imshow("Output", img)

cv2.waitKey(0)
'''

'''
#to capture the video
cap = cv2.VideoCapture(0)   # 0 - for default camera
cap.set(3,640)  # width
cap.set(4,480)  # height
cap.set(10,100)

while True:         #while loop because video is sequence of images
    success, img = cap.read()   #img= to read image, success = act like a vairiable for true and false
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ('q'):
        break
        
'''

#After the loop release the cap object
#cap.release()
#Destroy all the windows
cv2.destroyAllWindows()



