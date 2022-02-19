import cv2
import numpy as np
img = cv2.imread("colorwheel.png")
img = cv2.resize(img, (300, 300))
def detect_color(img2):
    cv2.imshow("original video",img2)
    lr = 200
    lg = 0
    lb = 0
    ur = 255
    ug = 50
    ub = 50
    lowerb = np.array([lb, lg, lr])
    upperb = np.array([ub, ug, ur])
    detect_red_color = cv2.inRange(img2, lowerb, upperb)
    rc = cv2.bitwise_and(img2, img2, mask=detect_red_color)
    cv2.imshow("detecting red color", detect_red_color)
    cv2.imshow("red", rc)
cap=cv2.VideoCapture("color.mp4")
while True:
    isTrue,img1=cap.read()
    img1=cv2.resize(img1,(400,400))
    detect_color(img1)
    cv2.waitKey(20)
cv2.imshow("wheel", img)
cv2.waitKey(0)
