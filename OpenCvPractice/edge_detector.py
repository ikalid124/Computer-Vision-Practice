import cv2 as cv
import os
import numpy as np

image = cv.imread("Kalid.jpg")

edge = cv.Canny(image, 100,200)
edge_thick = cv.dilate(edge,np.ones((3,3), dtype=np.int8))
edge_thin = cv.erode(edge,np.ones((3,3), dtype=np.int8))

cv.imshow("edge", edge )
cv.imshow("edge_thick", edge_thick )
cv.imshow("edge_thin", edge_thin )
cv.waitKey(0)






