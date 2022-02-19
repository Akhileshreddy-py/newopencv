import cv2
import numpy as np
img=cv2.imread("colorwheel.png")
img=cv2.resize(img,(300,300))
nimg=np.zeros((300,300,3),"uint8")
for i in range(300):
    for j in range(300):
        if img[i][j][0]<=50 and img[i][j][1]<=50 and img[i][j][2]>=200:
            nimg[i][j]=img[i][j]
cv2.imshow("black image",nimg)
cv2.imshow("wheel", img)
cv2.waitKey(0)