import cv2 as cv


img1 = cv.imread("1bit1.jpg") 
img2 = cv.imread("2bit2.jpg")

alpha_slider_max = 100
title_window = 'Linear Blend'
def on_trackbar(val):
    alpha = val / alpha_slider_max
    beta = ( 1.0 - alpha )
    dst = cv.addWeighted(img1, alpha, img2, beta, 0.0)
    cv.imshow(title_window, dst)


cv.namedWindow(title_window)

    
trackbar_name = 'Alpha x %d' % alpha_slider_max
cv.createTrackbar(trackbar_name, title_window , 0, alpha_slider_max, on_trackbar)
on_trackbar(0)
cv.waitKey(0)