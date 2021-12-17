from PIL import Image
import numpy as np
import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os
import sys
from convertTomp3 import convertToMp3
from videoMp3Combiner import videomp3combiner


def processVideo(inputVideo: str, outputVideo: str, subjectThreshold: float, backgroundThreshold: float):
    cap = cv2.VideoCapture(inputVideo)
    cap.set(3, 640)
    cap.set(4, 480)
    w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    if (cap.isOpened() == False):
        print("Error reading video file")
        sys.exit()

    segmentor = SelfiSegmentation(1)
    fpsReader = cvzone.FPS()
    ##
    fps = cap.get(cv2.CAP_PROP_FPS)

    print(
        "Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

    ##

    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter('output.mp4', fourcc, fps, (int(w), int(h)))

    while True:
        success, img = cap.read()
        if(success == True):

            # separating subject from video
            imgOut = segmentor.removeBG(
                img, (255, 255, 255), threshold=subjectThreshold)
            # img3 = cv2.absdiff(img, imgOut)#separating background from video
            img4 = cv2.bitwise_not(img)  # making the whole video negative
            img5 = segmentor.removeBG(
                imgOut, img4, threshold=backgroundThreshold)
            out.write(img5)
            # cv2.imshow("output", img5)
            # cv2.waitKey(1)
        else:
            break
    out.release()
    cap.release()
    cv2.destroyAllWindows()
    print(convertToMp3(inputVideo))
    videomp3combiner("output.mp4", "theaudio.mp3", outputVideo)

    os.remove(inputVideo)
    os.remove("output.mp4")
    os.remove("theaudio.mp3")
