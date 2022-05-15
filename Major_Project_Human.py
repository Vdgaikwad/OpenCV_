from cvzone.PoseModule import PoseDetector
import mediapipe as mp
import cv2
import time


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
while True:
    success, img = cap.read()
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)

    img = detector.findPose(img)
    #print(results)

    #if results.detections:
        #for id, detection in enumerate(results.detections):
            #print(detection.location_data.relative_bounding_box)
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False)
    (h, w) = img.shape[:2]
    (c, d) = (h // 2, w // 2)

    if bboxInfo:
        center = bboxInfo["center"]
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
        x, y = center
        te = change_to_angle(d - x, y - c)
        if k % 50 == 0:
            a = str(int(te))

            k += 1
        else:
            k += 1

    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
