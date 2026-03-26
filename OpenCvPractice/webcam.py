import cv2 as cv

#import/read webcam

webcam = cv.VideoCapture(0)

#visualize webcam


while True:
    ret, frames = webcam.read()
    cv.imshow("frames", frames)

    if cv.waitKey(40) & 0xFF == ord('q'):
        break

webcam.release()
cv.destroyAllWindows()