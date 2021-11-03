import cv2 as cv
# img = cv.imread("pic/1.jpg")
# cv.imshow('1', img)
# cv.waitKey(0)
cap=cv.VideoCapture('vid/1.mkv')
while(True):
 istrue,frame = cap.read()
 cv.imshow('1',frame)
 if cv.waitKey(20) & 0xFF==ord('d'):
  break
cap.release()


