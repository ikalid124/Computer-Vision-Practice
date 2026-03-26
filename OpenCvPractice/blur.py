import cv2 as cv
import os

img = cv.imread("kalid.jpg")
img_crop = img[0:500, 500:1000]


kernel_size = 11
img_blur = cv.blur(img_crop, (kernel_size,kernel_size))
img_GaussianBlur = cv.GaussianBlur(img_crop, (kernel_size,kernel_size),kernel_size)
img_medianBlur = cv.medianBlur(img_crop, kernel_size)

cv.imshow("img_blur", img_blur)
cv.imshow("img_GaussianBlur", img_GaussianBlur)
cv.imshow("img_medianBlur", img_medianBlur)
cv.waitKey(0)


