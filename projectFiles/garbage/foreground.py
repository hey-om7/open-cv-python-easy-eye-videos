# this code separates the foreground:subject from the background


import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os


cap = cv2.VideoCapture("vid.mp4")
cap.set(3, 640)
cap.set(4, 480)

segmentor = SelfiSegmentation(1)
fpsReader = cvzone.FPS()

while True:
    success, img = cap.read()
    imgOut = segmentor.removeBG(img, (0, 0, 0), threshold=0.55)

    imageStacked = cvzone.stackImages([img, imgOut], 2, 1)
    _, imageStacked = fpsReader.update(imageStacked, color=(0, 0, 255))
    cv2.imshow("Image Out", imgOut)

    cv2.waitKey(1)
