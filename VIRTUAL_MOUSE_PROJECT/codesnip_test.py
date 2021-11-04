import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
import numpy as np
image=np.zeros((1080,2160,3),dtype="uint8")
cv.rectangle(image,[75,75],[150,150],(0,0,255),-1)
cv.putText(image,"Q",(90,135),cv.FONT_ITALIC,2,(255,255,255),5)
cv.imshow("image",image)
cv.waitKey(0)