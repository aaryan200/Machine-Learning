import cv2
import mediapipe as mp
import time
import math

class poseDetector:
    def __init__(self,mode=False,modelComp=True,uBody=False,smooth=True,detectionCon=0.5,trackCon=0.5):
        self.mode=mode
        self.modelComp=modelComp
        self.uBody=uBody
        self.smooth=smooth
        self.detectionCon=detectionCon
        self.trackCon=trackCon
        self.mpDraw=mp.solutions.drawing_utils
        self.mpPose=mp.solutions.pose
        self.pose=self.mpPose.Pose(self.mode,self.modelComp,self.uBody,self.smooth,self.detectionCon,self.trackCon)
    
    def findPose(self,img,draw=True):
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img,self.results.pose_landmarks,self.mpPose.POSE_CONNECTIONS)
        return img
    def getPosition(self,img,draw=True):
        self.lmList=[]
        if self.results.pose_landmarks:
            for ids,lm in enumerate(self.results.pose_landmarks.landmark):
                h,w,c=img.shape
                cx,cy=int((lm.x)*w),int((lm.y)*h)
                self.lmList.append([ids,cx,cy])
                # print(ids,cx,cy)
                if draw:
                    cv2.circle(img,(cx,cy),7,(255,0,255),cv2.FILLED)
        return self.lmList
    def findAngle(self,img,p1,p2,p3,draw=True):
        x1,y1=self.lmList[p1][1:]
        x2,y2=self.lmList[p2][1:]
        x3,y3=self.lmList[p3][1:]
        angle=abs(math.degrees(math.atan2(y3-y2,x3-x2)-math.atan2(y1-y2,x1-x2)))
        if angle>180:
            angle=360-angle
        if draw:
            cv2.line(img,(x1,y1),(x2,y2),(0,0,0),3)
            cv2.line(img,(x3,y3),(x2,y2),(0,0,0),3)
            cv2.circle(img,(x1,y1),3,(0,0,255),cv2.FILLED)
            cv2.circle(img,(x1,y1),10,(0,0,255),3)
            cv2.circle(img,(x2,y2),3,(0,0,255),cv2.FILLED)
            cv2.circle(img,(x2,y2),10,(0,0,255),3)
            cv2.circle(img,(x3,y3),3,(0,0,255),cv2.FILLED)
            cv2.circle(img,(x3,y3),10,(0,0,255),3)
            cv2.putText(img,str(int(angle)),(x2-50,y2+30),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),2)
        return angle
def main():
    cap=cv2.VideoCapture(0)
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 120)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
    pTime=0
    cTime=0
    detector=poseDetector(uBody=True)
    while True:
        success,img=cap.read()
        img=detector.findPose(img)
        lmlist=detector.getPosition(img,draw=False)
        if len(lmlist)!=0:
            print(lmlist[14])
            cv2.circle(img,(lmlist[14][1],lmlist[14][2]),7,(255,0,255),cv2.FILLED)
        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime
        cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
        cv2.imshow("Frame",img)
        cv2.waitKey(5)
if __name__=='__main__':
    main()