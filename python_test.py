import cv2 # type: ignore
import numpy as np # type: ignore
import time
cap = cv2.VideoCapture(0)

width = 640
height = 480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


frame_count = 0
start_time = time.time()
while True:
    ret, frame = cap.read()
    if ret:
        frame_count+=1
        cv2.imshow('Video', frame)


    #cal time
    current_time=time.time()
    elapsed_time= current_time-start_time

    #cal fps
    fps=frame_count/elapsed_time
    if elapsed_time>1.0:
        print("FPS:", fps)
        frame_count = 0
        start_time = time.time()
    #quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()