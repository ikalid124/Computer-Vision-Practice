import os
import cv2 as cv
import numpy as np

#reading video

video_path = os.path.join('.', 'StoreVideos/Data', 'WIN_20241031_17_40_30_Pro.mp4')

video = cv.VideoCapture(video_path)
#visualising video

ret = True
while ret:
    ret, frame = video.read()

    if ret:
        cv.imshow('frame', frame)
        cv.waitKey(40)


video.release()
cv.destroyAllWindows()