import time
from datetime import datetime
import cv2
import keyboard
import threading




class Camera():
    def __init__(self) -> None:
        self.cap = cv2.VideoCapture(0)
        width = 1920
        height = 1080
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        pass

    def releaseSource(self):
        self.cap.release()
        cv2.destroyAllWindows()
    
    def formatTime(self,dateTimeStamp:float):
        resTime=datetime.fromtimestamp(dateTimeStamp)
        return resTime
def saveImage(pic_name,frame):
    res=cv2.imwrite("D:\\image\\{}.jpg".format(str(pic_name)),frame)

def printFPs(name,frame_count):
    print("thread:{} frame cout:{}".format(name,frame_count))

def Task():
    frame_count = 0
    start_time = time.time()
    camera=Camera()
    while True:
        ret, frame = camera.cap.read()
        current_time = time.time()
        if not ret:
            break
        frame_count += 1
        dt=camera.formatTime(current_time)
        pic_name="{}-{}-{}".format(dt.minute,dt.second,dt.microsecond)
        cv2.imshow('Video', frame)
        newthread = threading.Thread(target=saveImage,args=(pic_name,frame))
        newthread.start()  

        elapsed_time = current_time - start_time
        
        # Cal FPS
        fpsThread = threading.Thread(target=printFPs,args=(dt.second,frame_count))
        if elapsed_time > 1.00:
            start_time = time.time()
            fpsThread.start()  
            # print("frame cout:{}".format(frame_count))
            frame_count = 0
    
        # Quit
        if keyboard.is_pressed('q'):
            break


if __name__=="__main__":
    Task()
    pass