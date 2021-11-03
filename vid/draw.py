import cv2 as cv
import numpy as np
img=np.zeros((500,500,3),dtype="uint8")
#cv.imshow("blank",img)


# img[200:300,300:400]=0,0,255
# cv.imshow("blank_edit",img)




cv.rectangle(img,(0,0),(500,250),(100,150,100),thickness=-1)
#cv.imshow('rect',img)

cv.circle(img,(250,250),100,(0,0,250),thickness=-1)  #(width,height)
cv.imshow('rect',img)
cv.waitKey(0)

