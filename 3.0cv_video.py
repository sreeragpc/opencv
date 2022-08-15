import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = frame.shape[1] * scale
    height = frame.shape[0] * scale

capture = cv.VideoCapture("D:/machine learning/opencv/videoplayback (1).mp4")
#capture = cv.VideoCapture(0)
while True:
    istrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(1) & 0xFF==ord('q'):
        break
capture.release()
cv.destroyAllWindows  