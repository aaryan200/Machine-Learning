import cv2
import os
li = os.listdir('../../data/chessBot')
print(li)
for im in li:
    if (im[-1]=='g'):
        img = cv2.imread(f"../../data/chessBot/{im}")
        # change bgr to rgb
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # rotate image 90 degree anti-clockwise
        img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        # resize image
        img = cv2.resize(img, (512, 512))
        # crop image from center
        # img = img[100:300, 100:300]
        img = img[27:372, 40:479]
        cv2.imshow('image', img)
        cv2.waitKey(10000)