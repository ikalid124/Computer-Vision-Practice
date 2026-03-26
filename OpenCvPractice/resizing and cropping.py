import cv2 as cv
import os


image = cv.imread('kalid.jpg')

cv.imshow("kalid", image)





resized_image = cv.resize(image, (765,511 ))
cropped_img = image[0:500, 500:1000]

#  cv.imshow("kalid_resized", resized_image)
cv.imshow("cropped_img", cropped_img)


cv.waitKey(0)

print(image.shape)
print(resized_image.shape)



