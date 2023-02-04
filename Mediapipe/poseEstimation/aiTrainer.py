import cv2
import mediapipe as mp
import time
from poseModule import poseDetector

cap=cv2.VideoCapture('../data/21.jpg')
detector=poseDetector()
while True:
    success,img=cap.read()
    # if not success:
    #     print("Ignoring empty frame")
    #     continue
    h,w,c=img.shape
    img=cv2.resize(detector.findPose(img,draw=False),(500,int(500*h/w)))
    lmlist=detector.getPosition(img,draw=False)
    if len(lmlist):
        detector.findAngle(img,24,26,28)
    # if len(lmlist)!=0:
    #     print(lmlist[14])
    #     cv2.circle(img,(lmlist[14][1],lmlist[14][2]),7,(255,0,255),cv2.FILLED)
    # cTime=time.time()
    # fps=1/(cTime-pTime)
    # pTime=cTime
    # cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow("Frame",img)
    cv2.waitKey(10000)
if __name__=='__main__':
    main()