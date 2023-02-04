import cv2
import mediapipe as mp
import time
import numpy as np
import os
from HandTrackingModule import handDetector
import math

cap=cv2.VideoCapture(0)
detector=handDetector(maxHands=10)
while cap.isOpened():
    succ,img=cap.read()
    if not succ:
        print("Ignoring empty frame")
        continue
    img=detector.findHands(img)
    lmList=detector.findPosition(img,draw=False)
    ct=0
    if len(lmList):
        for hands in lmList:
            # print(hands)
            if hands[16][1]>hands[3][1]:
                if (hands[4][1]>hands[3][1]):
                    ct=ct
                else:
                    ct+=1
            else:
                if (hands[4][1]<hands[3][1]):
                    ct=ct
                else:
                    ct+=1
            for jt in range(6,19,4):
                if hands[jt+2][2]<hands[jt][2]:
                    ct+=1
    cv2.putText(img,str(ct),(10,70),cv2.FONT_HERSHEY_COMPLEX,3,(0,0,255),3)
    print(detector.fingersUp())
    cv2.imshow("Frame",img)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()