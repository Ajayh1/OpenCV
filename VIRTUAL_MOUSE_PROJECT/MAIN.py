from module import *


cap=cv.VideoCapture(0)
detector= HandDetector(maxHands=2,detectionCon=1)

cap.set(3,1080)
cap.set(4,2160)
while(True):
    isTrue,frame=cap.read()
    frame=detector.findHands(frame)
    lmList, bboxInfo = detector.findPosition(frame)
    image=cv.flip(frame,1)
    cv.imshow("Image",image)
    if cv.waitKey(1) & 0xff==ord("c"):
        break
cap.release()