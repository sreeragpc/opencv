import cv2 as cv

img = cv.imread('D:\machine learning\opencv\wp2359348-bmw-drift-wallpapers.jpg')
img = cv.resize(img,(200,200))
cv.imshow('bmw', img)
cv.waitKey(0)
