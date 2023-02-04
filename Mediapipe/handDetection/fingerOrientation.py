import time
import cv2
import mediapipe as mp
from HandTrackingModule import handDetector

def checkRightLeft(lm):
    n,x1,y1=lm[5] # finger bottom
    m,x2,y2=lm[8] # finger tip
    if (abs(x2-x1)<=1.0e-6):
        return False,False
    val=float((y2-y1)/(x2-x1))
    th = 0.75355405
    if (abs(val)<th):
        if (x2<x1):
            return True,False
        elif (x2>x1):
            return False,True
    return False,False

pTime=0
cTime=0
cap = cv2.VideoCapture(0)
detector=handDetector(maxHands=1)
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList=detector.findPosition(img,draw=False)
    if len(lmList):
        ch=checkRightLeft(lmList)
        if ch[0]:
            print("Finger is Right")
        elif ch[1]:
            print("Finger is Left")
        else:
            print("Finger is vertical")
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,255),3)

    cv2.imshow("Frame", img)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()