import cv2 as c
import numpy as np
camera=c.VideoCapture('rick_roll.mp4')

while True:
    val, frame=camera.read()
    frame=c.cvtColor(frame,c.COLOR_BGR2GRAY)
    frame=c.Canny(frame,50,50)
    kernil=np.ones((5,5),dtype='uint8')
    frame=c.dilate(frame,kernil,iterations=1) #????
    frame=c.erode(frame,kernil,iterations=1)
    c.imshow('camera',frame)
    if c.waitKey(28) & 0xFF==ord('q'):
        break
    