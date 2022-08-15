import cv2 as cv

img = cv.imread('D:\machine learning\opencv\wp2359348-bmw-drift-wallpapers.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#simple thresholding 
ret, thresh1 = cv.threshold(img, 120, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(img, 120, 255, cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(img, 120, 255, cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(img, 120, 255, cv.THRESH_TOZERO)
ret, thresh5 = cv.threshold(img, 120, 255, cv.THRESH_TOZERO_INV)

 

cv.imshow('Binary Threshold', thresh1)
cv.imshow('Binary Threshold Inverted', thresh2)
cv.imshow('Truncated Threshold', thresh3)
cv.imshow('Set to 0', thresh4)
cv.imshow('Set to 0 Inverted', thresh5)

#adaptive thresholding
thresh6 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY, 199, 5)  
thresh7 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY, 199, 5)
  
cv.imshow('Adaptive Mean', thresh6)
cv.imshow('Adaptive Gaussian', thresh7)



cv.imshow('bmw', img)

cv.waitKey(0)