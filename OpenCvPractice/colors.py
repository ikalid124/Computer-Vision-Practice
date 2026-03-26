import cv2 as cv
import os


#img = os.path.join('.','filename','img.jog')

#read image

img = cv.imread('kalid.jpg')

convert2grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('covnerted', convert2grey)
cv.imshow('kalid', img)
cv.waitKey(0)

