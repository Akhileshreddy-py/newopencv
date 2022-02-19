import cv2
import numpy as np
img = cv2.imread("colorwheel.png")
img = cv2.resize(img, (300, 300))
def detect_color():
    lr = 200
    lg = 0
    lb = 0
    ur = 255
    ug = 50
    ub = 50
    lowerb = np.array([lb, lg, lr])
    upperb = np.array([ub, ug, ur])
    detect_red_color = cv2.inRange(img, lowerb, upperb)
    rc = cv2.bitwise_and(img, img, mask=detect_red_color)
    cv2.imshow("detecting red color", detect_red_color)
    cv2.imshow("red", rc)
detect_color()
cv2.imshow("wheel", img)
cv2.waitKey(0)
