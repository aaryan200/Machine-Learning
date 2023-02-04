import cv2
import mediapipe as mp
import time
from faceDetecModule import FaceDetector
IMAGE_FILES = ['../data/abhishek.png','../data/IMG_6048.jpg','../data/IMG_6051.jpg','../data/IMG_6066.jpg','../data/IMG_6068.jpg','../data/IMG_6070.jpg','../data/IMG_6074.jpg','../data/IMG_6078.jpg','../data/IMG_6087.jpg']
detector=FaceDetector(minDetecCon=0.1)
print(len(IMAGE_FILES))
img = cv2.imread('../../../Videos/Muniya Reception/Photo/IMG_6391.jpg')
img = cv2.resize(img,(700,500))
img,li=detector.findFaces(img)
cv2.imshow("Image",img)
cv2.waitKey(5000)