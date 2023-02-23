import cv2 as c
import os

face_file=c.CascadeClassifier(os.path.join(c.data.haarcascades, 'haarcascade_frontalface_default.xml'))

#video=c.VideoCapture('tansuli.mp4')

video=c.VideoCapture(1)
video.set(3, 600)
video.set(4, 800)

while True:
    val, frame=video.read()
    video_gray=c.cvtColor(frame, c.COLOR_BGR2GRAY)
    face_coordinates=face_file.detectMultiScale(video_gray, 1.5, 2)
    for x, y, width, height in face_coordinates:
        c.rectangle(frame, (x, y), (x+width, y+height), (0, 0, 255), 1)
    c.imshow('camera', frame)
    if c.waitKey(0) & 0xFF==ord('q'):
        break
