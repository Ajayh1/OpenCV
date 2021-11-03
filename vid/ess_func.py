import cv2 as cv

img=cv.imread('../pic/2.jpeg')
cv.imshow('building',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('blackimg',gray)

blurr=cv.GaussianBlur(img,(51,51),cv.BORDER_DEFAULT)
cv.imshow('blurimg',blurr)
cannyy=cv.Canny(blurr,125,175)
cv.imshow('can',cannyy)
dilatee=cv.dilate(cannyy,(3,3),iterations=10)
cv.imshow("dilate",dilatee)
erodee=cv.erode(dilatee,(3,3),iterations=10)
cv.imshow('erode',erodee)
resize=cv.resize(img,(500,500))
cv.imshow("rez",resize)
crop=img[50:100,200:300]
cv.imshow('cropped',crop)

cv.waitKey(0)

