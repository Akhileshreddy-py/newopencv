import cv2
import numpy as np
img = cv2.imread("colorwheel.png")
img = cv2.resize(img, (300, 300))
cv2.imshow("wheel", img)
# cv2.namedWindow("")
def detect_color(p):
    lr =cv2.getTrackbarPos("lr","wheel")
    lg =cv2.getTrackbarPos("lg","wheel")
    lb =cv2.getTrackbarPos("lb","wheel")
    ur =cv2.getTrackbarPos("ur","wheel")
    ug =cv2.getTrackbarPos("ug","wheel")
    ub =cv2.getTrackbarPos("ub","wheel")
    lowerb = np.array([lb, lg, lr])
    upperb = np.array([ub, ug, ur])
    detect_red_color = cv2.inRange(img, lowerb, upperb)
    rc = cv2.bitwise_and(img, img, mask=detect_red_color)
    cv2.imshow("detecting red color", detect_red_color)
    cv2.imshow("red", rc)

cv2.createTrackbar("lr","wheel",0,255,detect_color)
cv2.createTrackbar("lg","wheel",0,255,detect_color)
cv2.createTrackbar("lb","wheel",0,255,detect_color)
cv2.createTrackbar("ur","wheel",0,255,detect_color)
cv2.createTrackbar("ug","wheel",0,255,detect_color)
cv2.createTrackbar("ub","wheel",0,255,detect_color)

cv2.imshow("wheel", img)
cv2.waitKey(0)
