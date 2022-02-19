import cv2
import numpy as np
nblack=np.zeros((400,400,3),"uint8")
cv2.imshow("black", nblack)
def cclr(p):
    r=cv2.getTrackbarPos("r", "black")
    g=cv2.getTrackbarPos("g", "black")
    b=cv2.getTrackbarPos("b", "black")
    nblack[:,:]=[r,g,b]
    cv2.imshow("black", nblack)
cv2.createTrackbar("r","black",0,255,cclr)
cv2.createTrackbar("g","black",0,255,cclr)
cv2.createTrackbar("b","black",0,255,cclr)
# print(nblack)
# nblack[:,:]=[255,230,0]
cv2.imshow("black", nblack)
cv2.waitKey(0)