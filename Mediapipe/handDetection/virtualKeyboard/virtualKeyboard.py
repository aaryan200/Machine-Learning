import cv2
import mediapipe as mp
import time
import numpy as np
import os
import sys
sys.path.append("D:\ML\ComputerVision\handDetection")
from HandTrackingModule import handDetector
import math
import ctypes
pTime=0
cTime=0
cap = cv2.VideoCapture(0)
user32 = ctypes.windll.user32
win_x, win_y = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
detector=handDetector(maxHands=1)
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    off_height, off_width = img.shape[:2]
    off_height /= 2
    off_width /= 2
    lmList=detector.findPosition(img,draw=False)
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,255),3)
    cv2.imshow("Frame", cv2.resize(img,(win_x, win_y)))
    cv2.moveWindow("Frame",0,0)
    # cv2.imshow("Frame",img)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
