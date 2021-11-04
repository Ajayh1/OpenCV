from module import *
class keyButtons():
    def __init__(self, pos, text, size=[75,75]):
        self.pos=pos
        self.size=size
        self.text=text
        
def drawkey(image,buttonObjList):
    for i in buttonObjList:
        x,y=i.pos
        w,h=i.size
        cv.rectangle(image,i.pos,[x+w,y+h],(0,0,255),-1)
        cv.putText(image,i.text,(i.pos[0]+15,i.pos[1]+60),cv.FONT_ITALIC,2,(255,255,255),5)
    return image
def onClick(lmList,buttonObjList,image,detector):
    
    if lmList:
        for butto in buttonObjList:
            x,y=butto.pos
            w,h=butto.size
            if x<lmList[8][0]<x+w and y<lmList[8][1]<y+h:
                cv.rectangle(image,butto.pos,[x+w,y+h],(0,0,139),-1)
                cv.putText(image,butto.text,(butto.pos[0]+15,butto.pos[1]+60),cv.FONT_ITALIC,2,(255,255,255),5)
                length,_,_=detector.findDistance(12,4,image)
                # print(length)
                
                if 0<length<40:
                
                    cv.rectangle(image,butto.pos,[x+w,y+h],(255,0,0),-1)
                    cv.putText(image,butto.text,(butto.pos[0]+15,butto.pos[1]+60),cv.FONT_ITALIC,2,(255,255,255),5)
                    sleep(0.15)
                    print(butto.text)