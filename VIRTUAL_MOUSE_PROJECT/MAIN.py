from module import *
from Func import *


cap=cv.VideoCapture(0)
detector= HandDetector(maxHands=2,detectionCon=1)
alphaList=[["Q","W","E","R","T","Y","U","I","O","P"],
            ["A","S","D","F","G","H","J","K","L",";"],
            ["Z","X","C","V","B","N","M",",",".","/"]]


cap.set(3,1080)
cap.set(4,2160)
buttonObjList=[]
for x in range(len(alphaList)):
    for i,k in enumerate(alphaList[x]):
        buttonObjList.append(keyButtons([100*i+200,100*x+200],k))


while(True):
    isTrue,image=cap.read()
    image=cv.flip(image,1)
    image=detector.findHands(image)
    lmList, bboxInfo = detector.findPosition(image)
    
    drawkey(image,buttonObjList)
    onClick(lmList,buttonObjList,image,detector)
    
    cv.imshow("Image",image)
    
    if cv.waitKey(1) & 0xff==ord("c"):
        break
cap.release()