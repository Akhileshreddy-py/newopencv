import cv2
import numpy as np
img = cv2.imread("colorwheel.png")
img = cv2.resize(img, (300, 300))
lowerb=0
upperb=0
def ftrack(p):
    global lowerb,upperb;
    lr =cv2.getTrackbarPos("lr","wheel")
    lg =cv2.getTrackbarPos("lg","wheel")
    lb =cv2.getTrackbarPos("lb","wheel")
    ur =cv2.getTrackbarPos("ur","wheel")
    ug =cv2.getTrackbarPos("ug","wheel")
    ub =cv2.getTrackbarPos("ub","wheel")
    lowerb = np.array([lb, lg, lr])
    upperb = np.array([ub, ug, ur])
    
def detect_color(img2):
    cv2.imshow("original video",img2)
    detect_red_color = cv2.inRange(img2, lowerb, upperb)
    rc = cv2.bitwise_and(img2, img2, mask=detect_red_color)
    hc=cv2.hconcat([img2,rc])
    cv2.imshow("horizantal ",hc)
    cv2.imshow("detecting red color", detect_red_color)
    cv2.imshow("red", rc)
cap=cv2.VideoCapture("color.mp4")
cv2.imshow("wheel", img)
cv2.createTrackbar("lr","wheel",0,255,ftrack)
cv2.createTrackbar("lg","wheel",0,255,ftrack)
cv2.createTrackbar("lb","wheel",0,255,ftrack)
cv2.createTrackbar("ur","wheel",0,255,ftrack)
cv2.createTrackbar("ug","wheel",0,255,ftrack)
cv2.createTrackbar("ub","wheel",0,255,ftrack)
cv2.imshow("wheel", img)
while True:
    isTrue,img1=cap.read()
    img1=cv2.resize(img1,(400,400))
    detect_color(img1)
    cv2.waitKey(20)
cv2.imshow("wheel", img)
cv2.waitKey(0)
