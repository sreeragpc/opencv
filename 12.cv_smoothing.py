import cv2 as cv

img = cv.imread('D:\machine learning\opencv\wp2359348-bmw-drift-wallpapers.jpg')

smooth = cv.blur(img, (3, 3))
 

cv.imshow('bmw', img)
cv.imshow('bmw_smooth', smooth)
cv.waitKey(0)