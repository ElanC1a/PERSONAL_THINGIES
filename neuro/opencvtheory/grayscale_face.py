import cv2 as c
import numpy as np

camera=c.VideoCapture(0)
camera.set(3,600)
camera.set(4,800)

while True:
    val, frame=camera.read()
    canvas=np.ones((5,5), dtype='uint8')

    frame=c.cvtColors(frame, c.COLOR_BGR2GRAY)
    frame=c.GaussianBlur(frame, (5,7), 0)
    frame=c.Canny(frame, 50, 50)

    matrix_conturing, hierarchy=c.findContours(frame, c.RETR_LIST, c.CHAIN_APPROX_NONE)

    c.drawContours(canvas, matrix_conturing, -1, (180, 0, 99), 1)
    # frame=c.dilate(frame, kernil, iterations=1)
    # frame=c.erode(frame, kernil, iterations=1)

    c.imshow('camera',frame)
    if c.waitKey(1) & 0xFF==ord('q'):
        break