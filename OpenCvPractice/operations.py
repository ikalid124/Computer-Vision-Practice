import numpy as np
import cv2 as cv

#read image
img = cv.imread('kalid.jpg')
assert img is not None, "file couldnt be read"

#write image
cv.imwrite("kalid_out.jpg", img)

#visualizing image
cv.imshow("image", img) #shows image in a new tab
cv.waitKey(0)#stops it from immediately closing



#n = np.array = [1,2,3]


#px = img[100,100]
#print(px) #retunrs pixel values rgb at 100,100


#blue = img[100,100,0]  # img[x,y,channel/color]
# 0 = Blue, 1 = Green, 2 = Red
#print(blue)


#print(img.shape) #shape
#print(img.size) #size
#print(img.dtype) #datatype


#eyes = img[280:340, 330:390] # looking at regions (region of images(ROI))

