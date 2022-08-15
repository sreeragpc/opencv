import cv2 as cv
import datetime

capture = cv.VideoCapture("D:/machine learning/opencv/videoplayback (1).mp4")

while True:
    istrue, frame = capture.read()

    font = cv.FONT_HERSHEY_SIMPLEX
    dt = datetime.datetime.now()
    dt = str(dt)
    cv.putText(frame,dt 
                , 
                (20, 300), 
                font, 1, 
                (0, 0, 255), 
                2, 
                cv.LINE_4)
  
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('q'):
        break
capture.release()
cv.destroyAllWindows  