import cv2 
import matplotlib.pyplot as plt 
import numpy as np

image = cv2.imread('morphologiacal.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(12, 12))
plt.subplot(3, 2, 1)
plt.title("Original")
plt.imshow(image)

kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(image, kernel, iterations = 1)
plt.subplot(3, 2, 2)
plt.title("Erosion")
plt.imshow(erosion)
dilation = cv2.dilate(image, kernel, iterations = 1)
plt.subplot(3, 2, 3)
plt.title("Dilation")
plt.imshow(dilation)


opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
plt.subplot(3, 2, 4)
plt.title("Opening")
plt.imshow(opening)

plt.show()