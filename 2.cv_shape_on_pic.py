import cv2 as cv

img = cv.imread('D:\machine learning\opencv\wp2359348-bmw-drift-wallpapers.jpg')
img = cv.line(img, (0,700), (1000,700), (0,0,248), 4)
img = cv.rectangle(img, (50,600), (250,650), (240,0,248), 4)
img = cv.circle(img, (300,300), 60, (0,0,250), 2) 

cv.imshow('bmw', img)
cv.waitKey(0)