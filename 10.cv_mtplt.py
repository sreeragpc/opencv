import cv2 as cv
import matplotlib.pyplot as plt 

img = cv.imread("D:\machine learning\opencv\wp2359348-bmw-drift-wallpapers.jpg")


plt.imshow(img)
plt.show()
cv.waitKey(0)