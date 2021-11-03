import cv2 as cv


def rescaleFrame(frame, scale=0.50):
    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

cap=cv.VideoCapture('./1.mkv')
while(True):
    istrue, frame = cap.read()
    frame_resized = rescaleFrame(frame)
   #cv.imshow('1',frame)
    cv.imshow('1_resize', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
cap.release()
cv.destroyAllWindows()

