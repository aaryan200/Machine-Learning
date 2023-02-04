import cv2
import mediapipe as mp
import time

mpDraw=mp.solutions.drawing_utils
mpPose=mp.solutions.pose
pose=mpPose.Pose()

cap=cv2.VideoCapture('data/8.mp4')
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 120)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
pTime=0
cTime=0
while True:
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=pose.process(imgRGB)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for ids,lm in enumerate(results.pose_landmarks.landmark):
            h,w,c=img.shape
            cx,cy=int((lm.x)*w),int((lm.y)*h)
            print(ids,cx,cy)
            cv2.circle(img,(cx,cy),25,(255,0,255),cv2.FILLED)
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow("Frame",img)
    cv2.waitKey(5)
