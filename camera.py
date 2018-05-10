#! py -3
# -*- coding: utf-8 -*-

import cv2

clicked = False


def on_mouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True


cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow("windy")
cv2.setMouseCallback("windy", on_mouse)

print("Showing camera feed. Click window or press any key to stop.")

sucess, frame = cameraCapture.read()

while sucess and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow("windy", frame)
    sucess, frame = cameraCapture.read()

cv2.destroyWindow("windy")
cameraCapture.release()


