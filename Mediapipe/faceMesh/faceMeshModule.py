import cv2
import mediapipe as mp
import time

class FaceMeshDetector:
    def __init__(self,staticMode=False,maxFaces=2,refLandm=False,minDetectionCon=0.5,minTrackCon=0.5):
        self.staticMode=staticMode
        self.maxFaces=maxFaces
        self.refLandm=refLandm
        self.minDetectionCon=minDetectionCon
        self.minTrackCon=minTrackCon
        self.mpFaceMesh=mp.solutions.face_mesh
        self.mpDraw=mp.solutions.drawing_utils
        self.faceMesh=self.mpFaceMesh.FaceMesh(self.staticMode,self.maxFaces,self.refLandm,self.minDetectionCon,self.minTrackCon)
        self.drawSpec=self.mpDraw.DrawingSpec(color=(61, 252, 3),thickness=1,circle_radius=1)

    def findFaceMesh(self,img,draw=True):
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.faceMesh.process(imgRGB)
        faces=[]
        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,faceLms,self.mpFaceMesh.FACEMESH_CONTOURS,landmark_drawing_spec=self.drawSpec,
                                        connection_drawing_spec=self.drawSpec)
                face=[]
                for ids,lm in enumerate(faceLms.landmark):
                    ih,iw,ic=img.shape
                    x,y=int(lm.x*iw),int(lm.y*ih)
                    # cv2.putText(img,str(ids),(x,y),cv2.FONT_HERSHEY_PLAIN,0.7,(61, 252, 3),1)
                    face.append([x,y])
                faces.append(face)
        return img,faces

def main():
    cap=cv2.VideoCapture(0)
    ptime=0
    ctime=0
    detector=FaceMeshDetector(maxFaces=2)
    while True:
        success, img=cap.read()
        img,li=detector.findFaceMesh(img)
        if len(li)!=0:
            print(len(li))
        ctime=time.time()
        fps=1/(ctime-ptime)
        ptime=ctime
        cv2.putText(img,f'FPS: {int(fps)}',(20,20),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),2)
        cv2.imshow("Image",img)
        cv2.waitKey(5)
    cap.release()
    cv2.destroyAllWindows()


if __name__=='__main__':
    main()