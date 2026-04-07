import cv2 as cv



webcam = cv.VideoCapture(0)
print(webcam.isOpened())

while True:

    ret, frames = webcam.read()
    
    if not ret:
     break
    #ret, thresh = cv.threshold(frames, 80, 255, cv.THRESH_BINARY)
    gray_image = cv.cvtColor(frames, cv.COLOR_BGR2GRAY)
    adaptive_thresh = cv.adaptiveThreshold(gray_image,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,21,30)
    #blur_web = cv.blur(thresh, (10,10))

    #blur_web = cv.medianBlur(adaptive_thresh, 9)
    cv.imshow("original", frames)
    cv.imshow("gray", gray_image)
    cv.imshow("blur_web", adaptive_thresh)

    if cv.waitKey(40) & 0xFF == ord("q"):
        break

webcam.release()
cv.destroyAllWindows()
