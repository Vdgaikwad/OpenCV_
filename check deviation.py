import numpy as np
from cvzone.PoseModule import PoseDetector
import cv2
import time

#
tolerance=0.1
x_deviation=0
y_max=0
arr_track_data=[0,0,0,0,0,0]
#

def change_to_angle(x, y):
    pan = -0.07813 * x
    # tilt= 45 + (90*y/height)
    return (pan)


cap = cv2.VideoCapture(0)
detector = PoseDetector()

pTime = 0
cTime = 0

prev = 90
k = 50

#-------initialise motor speed---------
# import RPi.GPIO as GPIO
#
# GPIO.setmode(GPIO.BCM)  # choose BCM numbering scheme
#
# GPIO.setup(20, GPIO.OUT)  # set GPIO 20 as output pin
# GPIO.setup(21, GPIO.OUT)  # set GPIO 21 as output pin
#
# pin20 = GPIO.PWM(20, 100)  # create object pin20 for PWM on port 20 at 100 Hertz
# pin21 = GPIO.PWM(21, 100)  # create object pin21 for PWM on port 21 at 100 Hertz
#
# val = 100
# pin20.start(val)  # start pin20 on 0 percent duty cycle (off)
# pin21.start(val)  # start pin21 on 0 percent duty cycle (off)
#
# print("speed set to: ", val)

while True:
    success, img = cap.read()
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
   #

    cv2_im = img

    #
    img = detector.findPose(img)

    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False)

    (h, w) = img.shape[:2]
    #print("height",h,"width",w)
    #height = 480; width = 640
    (c, d) = (h // 2, w // 2)
    #print(c,d) #c=240; d=320
    # draw center cross lines
    cv2_im = cv2.rectangle(cv2_im, (0, int(h / 2) - 1), (w, int(h / 2) + 1), (255, 0, 0), -1)
    cv2_im = cv2.rectangle(cv2_im, (int(w / 2) - 1, 0), (int(w / 2) + 1, h), (255, 0, 0), -1)

    # draw the center red dot on the object
    cv2_im = cv2.circle(cv2_im, (int(arr_track_data[0] * w), int(arr_track_data[1] * h)), 7, (0, 255, 255), -1)

    if bboxInfo:
        #bboxInfo - "id","bbox","score","center"
       ## center = bboxInfo["center"]

        #
        x_min, y_min, x_max, y_max = bboxInfo["bbox"]
        print(x_min, y_min, x_max, y_max)

        #
        

#----------for finding the deviation ----------------#
        x_diff = x_max-x_min
        y_diff = y_max - y_min
        print("x_diff: ",round(x_diff,5))
        print("y_diff: ",round(y_diff,5))

        obj_x_center = x_min+(x_diff/2)
        obj_x_center = round(obj_x_center,3)

        obj_y_center = y_min + (y_diff / 2)
        obj_y_center = round(obj_y_center, 3)

        #print("[", obj_x_center, obj_y_center, "]")
        #cv2.circle(img,(obj_x_center, obj_y_center),5,(0,255,0),cv2.FILLED)

        x_deviation = round(c-obj_x_center,3)
        y_deviation = round(d-obj_y_center,3)


        print("{",x_deviation,y_deviation,"}")

        arr_track_data[0] = obj_x_center
        arr_track_data[1] = obj_y_center
        arr_track_data[2] = x_deviation
        arr_track_data[3] = y_max



        #

        #print('bbox', bbox)
       ##cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
        ##x, y = center
        ## te = change_to_angle(d - x, y - c)
        ## if k % 50 == 0:
        ##     a = str(int(te))
        ##
        ##     k += 1
        ## else:
        ##     k += 1

    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()