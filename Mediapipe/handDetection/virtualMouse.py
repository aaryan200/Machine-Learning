from enum import auto
import cv2
import mediapipe as mp
import time
import numpy as np
import os
from HandTrackingModule import handDetector
import math
import autopy
wScr,hScr=autopy.screen.size()
# print(wScr,hScr)
cap = cv2.VideoCapture(0)
wCam,hCam=640,480
cap.set(3,wCam)
cap.set(4,hCam)
detector=handDetector(maxHands=1)
frameR=100
smoothening=7
plocX,plocY=0,0
clocX,clocY=0,0
while True:
    suc,img=cap.read()
    img=detector.findHands(img)
    lmList=detector.findPosition(img,draw=False)
    if len(lmList):
        x1,y1=lmList[8][1:]
        x2,y2=lmList[12][1:]
        fingers=detector.fingersUp()
        cv2.rectangle(img,(frameR,frameR),(wCam-frameR,hCam-frameR),(255,0,255),2)
        # Only index finger: moving mode
        if fingers[1]==1 and fingers[2]==0:
            # Convert coordinates
            x3,y3=np.interp(x1,(frameR,wCam-frameR),(0,wScr)),np.interp(y1,(frameR,hCam-frameR),(0,hScr))
            clocX=plocX+(x3-plocX)/smoothening
            clocY=plocY+(y3-plocY)/smoothening
            if 0<clocX< wScr and 0<clocY<hScr:
                autopy.mouse.move(wScr-clocX,clocY)
            cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
            plocX,plocY=clocX,clocY
        # Clicking mode
        elif fingers[1]==1 and fingers[2]==1:
            length,img,lineInfo=detector.findDistance(img,8,12)
            # print(length)
            if length<40:
                cv2.circle(img,(lineInfo[4],lineInfo[5]),15,(0,255,0),cv2.FILLED)
                autopy.mouse.click()
    cv2.imshow("Frame",img)
    cv2.waitKey(10)