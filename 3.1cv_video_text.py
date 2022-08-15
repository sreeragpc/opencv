import cv2 as cv

capture = cv.VideoCapture("D:/machine learning/opencv/videoplayback (1).mp4")

while True:
    istrue, frame = capture.read()

    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(frame, 
                'birdieeeeeeeeee', 
                (20, 300), 
                font, 1, 
                (0, 0, 255), 
                3, 
                cv.LINE_4)
  
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('q'):
        break
capture.release()
cv.destroyAllWindows  