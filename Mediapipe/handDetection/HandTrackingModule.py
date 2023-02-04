# If you place a hand after another hand then the initial hand's landmarks will be given in lmList[1] i.e.
# it will treat initial hand as 2nd hand

import cv2
import mediapipe as mp
import time
import ctypes
import math
class handDetector:
    def __init__(self,mode=False,maxHands=2,modelComp=True,detectionCon=0.5,trackCon=0.5):
        self.mode=mode
        self.maxHands=maxHands
        self.detectionCon=detectionCon
        self.trackCon=trackCon
        self.modelComp=modelComp
        self.mpHands=mp.solutions.hands
        self.hands=self.mpHands.Hands(self.mode,self.maxHands,self.modelComp,self.detectionCon,self.trackCon)
        self.mpDraw=mp.solutions.drawing_utils
        self.tipIds=[8,12,16,20]
    def findHands(self,img,draw=True):
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # hands only takes RGB images
        self.results=self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,handLms,self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self,img,draw=True):
        if self.maxHands==1:
            self.lmList=[]
            if self.results.multi_hand_landmarks:
                myHand=self.results.multi_hand_landmarks[0]
                for ids,lm in enumerate(myHand.landmark):
                    # print(id,lm)
                    h,w,c=img.shape
                    cx,cy=int((lm.x)*w),int((lm.y)*h)
                    # print(ids,cx,cy)
                    self.lmList.append([ids,cx,cy])
                    if draw:
                        cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)
            return self.lmList
        elif self.maxHands>=2:
            self.lmList=[]
            if self.results.multi_hand_landmarks:
                # myHand=self.results.multi_hand_landmarks[handNo]
                for myHand in self.results.multi_hand_landmarks:
                    lml=[]
                    for ids,lm in enumerate(myHand.landmark):
                        # print(id,lm)
                        h,w,c=img.shape
                        cx,cy=int((lm.x)*w),int((lm.y)*h)
                        # print(ids,cx,cy)
                        lml.append([ids,cx,cy])
                        if draw:
                            cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)
                    self.lmList.append(lml)
            return self.lmList
    def fingersUp(self):
        self.fingers=[]
        if len(self.lmList):
            if self.maxHands==1:
                if self.lmList[16][1]>self.lmList[3][1]:
                    if (self.lmList[4][1]>self.lmList[3][1]):
                        self.fingers.append(0)
                    else:
                        self.fingers.append(1)
                else:
                    if (self.lmList[4][1]<self.lmList[3][1]):
                        self.fingers.append(0)
                    else:
                        self.fingers.append(1)
                for jt in self.tipIds:
                    if self.lmList[jt][2]<self.lmList[jt-2][2]:
                        self.fingers.append(1)
                    else:
                        self.fingers.append(0)
                return self.fingers
            elif self.maxHands>1:
                for ids,hands in enumerate(self.lmList):
                    fing=[]
                    if hands[16][1]>hands[3][1]:
                        if (hands[4][1]>hands[3][1]):
                            fing.append(0)
                        else:
                            fing.append(1)
                    else:
                        if (hands[4][1]<hands[3][1]):
                            fing.append(0)
                        else:
                            fing.append(1)
                    for jt in self.tipIds:
                        if hands[jt][2]<hands[jt-2][2]:
                            fing.append(1)
                        else:
                            fing.append(0)
                    self.fingers.append([ids,fing])
                return self.fingers
        return self.fingers
    def findDistance(self,img,p1,p2,draw=True,handNo=0,r=15,t=3):
        if self.maxHands==1:
            x1,y1=self.lmList[p1][1:]
            x2,y2=self.lmList[p2][1:]
            cx,cy=(x1+x2)//2, (y1+y2)//2
            if draw:
                cv2.line(img,(x1,y1),(x2,y2),(255,0,255),t)
                cv2.circle(img,(x1,y1),r,(255,0,255),cv2.FILLED)
                cv2.circle(img,(x2,y2),r,(255,0,255),cv2.FILLED)
                cv2.circle(img,(cx,cy),r,(0,0,255),cv2.FILLED)
            length=math.hypot(x2-x1,y2-y1)
            return length,img,[x1,y1,x2,y2,cx,cy]

# mpHands=mp.solutions.hands
# hands=mpHands.Hands()
# mpDraw=mp.solutions.drawing_utils




def main():
    pTime=0
    cTime=0
    cap = cv2.VideoCapture(0)
    # wCam=1920
    # hCam=1080
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, wCam)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, hCam)
    user32 = ctypes.windll.user32
    win_x, win_y = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
    # win_cnt_x, win_cnt_y = [user32.GetSystemMetrics(0)/2, user32.GetSystemMetrics(1)/2]
    maxh=2
    detector=handDetector(maxHands=maxh)
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        off_height, off_width = img.shape[:2]
        off_height /= 2
        off_width /= 2
        lmList=detector.findPosition(img,draw=False)
        if maxh==1 and len(lmList):
            print(lmList[4])
        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime

        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,255),3)
        if maxh>1 and len(lmList)>1:
            cv2.circle(img,(lmList[1][8][1],lmList[1][8][2]),10,(255,0,255),cv2.FILLED)
        cv2.imshow("Frame", cv2.resize(img,(win_x, win_y)))
        cv2.moveWindow("Frame",0,0)
        # cv2.imshow("Frame",img)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

if __name__=="__main__":
    main()