import cv2 as cv
  
cam = cv.VideoCapture(0)

result, image = cam.read()

if result:

	cv.imshow("image", image)

	cv.imwrite("newwwwww.png", image)
    
cv.waitKey(0)
cv.destroyWindow("image")


