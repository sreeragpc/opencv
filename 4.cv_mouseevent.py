import cv2 as cv 

img  = cv.imread("wp2359348-bmw-drift-wallpapers.jpg")
cv.imshow('image', img)

def mouse_click(event, x, y, 
                flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
          
        font = cv.FONT_HERSHEY_TRIPLEX
        LB = '--> Left button'
        cv.putText(img, LB, (x, y), 
                    font, 1, 
                    (255, 0, 0), 
                    2) 
        cv.imshow('image', img)

    if event == cv.EVENT_RBUTTONDOWN:
           
        font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
        RB = '-->Right button'
        cv.putText(img, RB, (x, y),
                    font, 1, 
                    (0, 0, 255),
                    2)
        cv.imshow('image', img)
  
cv.setMouseCallback('image', mouse_click)
   
cv.waitKey(0)

cv.destroyAllWindows()