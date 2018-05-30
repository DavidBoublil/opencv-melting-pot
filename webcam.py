import cv2
import numpy as np


# def wbcam(miror=False):
THRESH = 100
ADAPTRHESH = 15


def nothing(positional):
    pass

cv2.namedWindow('control')
factor = 20
uh = 100
us = 100
uv = 100


def update_uh(val):
    global uh
    uh = val


def update_us(val):
    global us
    us = val


def update_uv(val):
    global uv
    uv = val


def update_factor(val):
    global factor
    factor = val

cv2.createTrackbar('Up Hue', 'control', 10, 255, update_uh)
cv2.createTrackbar('Up Sat', 'control', 10, 255, update_us)
cv2.createTrackbar('Up val', 'control', 10, 255, update_uv)
cv2.createTrackbar('factor', 'control', 2, 150, update_factor)

cam = cv2.VideoCapture(0)

while True:
    _, org_img = cam.read(1)
    org_img = cv2.flip(org_img, 1)
    blur = cv2.GaussianBlur(org_img, (5, 5), 0)
    hsv = cv2.cvtColor(org_img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, np.array([uh - factor, us - factor, uv - factor]), np.array([uh + factor, us + factor, uv + factor]))
    filtered = cv2.bitwise_and(org_img, org_img, mask=mask)
    cv2.imshow('control', filtered)

    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
