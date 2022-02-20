import cv2
import numpy as np
cv2.namedWindow("oimg")
oimg=cv2.imread("e4.jpg")
img=cv2.cvtColor(oimg,cv2.COLOR_BGR2GRAY)
def t(p):
    ps=cv2.getTrackbarPos("th","oimg")
    _,timg=cv2.threshold(img,ps,255,cv2.THRESH_BINARY)
    cv2.imshow("timg",timg)
    cnts,hier=cv2.findContours(timg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    print(len(cnts))
    print("cnts :",cnts[1])
    img1=cv2.drawContours(oimg,cnts,-1,(0,0,255),4)
    cv2.imshow("img1",img1)
    img1[:]=0   #black image 
    # print(timg)
    # cv2.imshow("oimg",img)
cv2.createTrackbar("th","oimg",0,255,t)
cv2.imshow("oimg",img)
cv2.waitKey(0)