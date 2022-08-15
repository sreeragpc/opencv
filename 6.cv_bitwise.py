import cv2 as cv
from cv2 import waitKey
img1 = cv.imread("1bit1.jpg") 
img2 = cv.imread("2bit2.jpg")

and_pic = cv.bitwise_and(img2, img1, mask=None)
or_pic = cv.bitwise_or(img2, img1, mask=None)
not_pic = cv.bitwise_not(img2, img1, mask=None)
xor_pic =cv.bitwise_xor(img2, img1, mask=None)
cv.imshow('image1', img1)
cv.imshow('image2', img2)

cv.imshow('and', and_pic)
cv.imshow('or',or_pic)
cv.imshow('xor',xor_pic)


waitKey(0)