from email import header
import cv2
import mediapipe as mp
import time
import numpy as np
import os
from HandTrackingModule import handDetector
import math

rawImg=os.listdir('img/')
# print(rawImg)
ImgList=[]
for imgs in rawImg:
    ImgList.append(cv2.imread(f'img/{imgs}'))
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,800)
brushThickness=15
eraserThickness=50
xp,yp=0,0
header=ImgList[0]
drawColor=(0,0,255)
detector=handDetector(detectionCon=0.7,maxHands=1) # 2d landmark list
imgCanvas=np.zeros((800,1280,3),np.uint8)
while True:
    suc,img=cap.read()
    img=cv2.resize(img,(1280,800))
    img=cv2.flip(img,1)
    img=detector.findHands(img)
    lmList=detector.findPosition(img,draw=False)
    if len(lmList):
        x1,y1=lmList[8][1:]
        x2,y2=lmList[12][1:]
        fingers=detector.fingersUp()
        # Selection mode
        if fingers[1] and fingers[2]:
            xp,yp=0,0
            if y1<105:
                if 0<x1<256:
                    header=ImgList[0]
                    drawColor=(0,0,255) # BGR
                elif 256<x1<512:
                    header=ImgList[1]
                    drawColor=(255,0,255)
                elif 512<x1<768:
                    header=ImgList[2]
                    drawColor=(255,71,52)
                elif 768<x1<1024:
                    header=ImgList[3]
                    drawColor=(0,255,0)
                elif 1024<x1<1280:
                    header=ImgList[4]
                    drawColor=(0,0,0)
            elif 115<y1<195:
                if 0<x1<200:
                    imgCanvas=np.zeros((800,1280,3),np.uint8)
                    img[0:105,0:1280]=header
                    img[115:195,0:200]=ImgList[5]
                    cv2.imshow("Frame",img)
                    cv2.waitKey(5)
                    continue
            cv2.rectangle(img,(x1,y1-25),(x2,y2+30),drawColor,cv2.FILLED)
        # Drawing mode
        if fingers[1] and fingers[2]==False:
            if xp==0 and yp==0:
                xp,yp=x1,y1
            if drawColor==(0,0,0):
                cv2.line(imgCanvas,(xp,yp),(x1,y1),drawColor,eraserThickness)
                cv2.circle(img,(x1,y1),eraserThickness,drawColor,cv2.FILLED)
            else:
                cv2.line(imgCanvas,(xp,yp),(x1,y1),drawColor,brushThickness)
                cv2.circle(img,(x1,y1),brushThickness,drawColor,cv2.FILLED)
            xp,yp=x1,y1,
    imgGray=cv2.cvtColor(imgCanvas,cv2.COLOR_BGR2GRAY) 
    _, imgInv=cv2.threshold(imgGray,50,255,cv2.THRESH_BINARY_INV)# Black and white version of imgCanvas
    imgInv=cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)
    img=cv2.bitwise_and(img,imgInv)# Make black portion in original image
    img=cv2.bitwise_or(img,imgCanvas)# Make colored portion in original image
    img[0:105,0:1280]=header
    img[115:195,0:200]=ImgList[5]
    cv2.imshow("Frame",img)
    # cv2.imshow("Gray",imgGray)
    cv2.waitKey(5)