# this code separates the background from the subject

from PIL import Image
import numpy as np
import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os


# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("vid.mp4")
cap.set(3, 640)
cap.set(4, 480)

segmentor = SelfiSegmentation(1)
fpsReader = cvzone.FPS()

while True:
    success, img = cap.read()
    imgOut = segmentor.removeBG(img, (0, 0, 0), threshold=0.55)
    img3 = cv2.absdiff(img, imgOut)
    img4 = cv2.bitwise_not(img3)
    cv2.imshow("Image Out", img4)
    # cv2.imshow("Image Out", imageStacked)

    cv2.waitKey(1)


# capture = cv2.VideoCapture("vid.mov")
# while True:
#     f, frame = capture.read()
#     frame = cv2.GaussianBlur(frame, (15, 15), 0)
#     frame = frame
#     cv2.imshow("window", frame)
