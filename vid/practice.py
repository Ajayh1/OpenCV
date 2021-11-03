import cv2 as cv
import numpy as np
# picture=cv.imread("1.jpg")
# cv.imshow("picture",picture)
# cv.waitKey(0)
# video=cv.VideoCapture("1.mkv")
# while(True):
#     istrue,frame = video.read()
#     cv.imshow('Video',frame)
#     if cv.waitKey(20) and 0xFF==ord('d'):
#         break
# video.Release()
# def Resize(frame,scale=0.5):
#     h = int(frame.shape[0]*scale)
#     w = int(frame.shape[1]*scale)
#     dim = (w,h)
#     return cv.resize(frame,dim,interpolation=cv.INTER_AREA)
# picture=cv.imread("1.jpg")
# img_res = Resize(picture)
# cv.imshow("picture",img_res)
# while(True):
#     if cv.waitKey(20) & 0xFF == ord('a'):
#         break
img=np.zeros((500,1000,3),dtype='uint8')
# cv.imshow('img',img)


cv.rectangle(img,(0,0),(500,250),(0,255,250),thickness=10)
cv.imshow('rectangle',img)
cv.waitKey(0)


