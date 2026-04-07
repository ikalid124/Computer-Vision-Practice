import cv2 as cv




photo = cv.imread("kalid.jpg")
print(photo.shape)
#line
cv.line(photo,(500,500), (1000,500), (50,100,50), 2)
cv.line(photo,(1000,500), (650,10), (50,100,50), 2)
cv.line(photo,(500,500), (650,10), (50,100,50), 2)


#text
cv.putText(photo, "Boy SLow Down", (1000,200), cv.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 3)



#rect
cv.rectangle(photo, (200,200), (400,400), (1,2,3), 5)

#circle
cv.circle(photo, (1000,700), 30, (255,255,0), 5)

cv.imshow("name", photo)
cv.waitKey(0)