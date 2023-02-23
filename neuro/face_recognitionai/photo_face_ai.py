import cv2 as c 
import os

face_file=c.CascadeClassifier(os.path.join(c.data.haarcascades, 'haarcascade_frontalface_default.xml'))

picture=c.imread('multiple_faces.jpg')
picture_gray=c.cvtColor(picture, c.COLOR_BGR2GRAY)

face_coordinates=face_file.detectMultiScale(picture_gray, 5, 5) # scale, neighbor

for x, y, width, height in face_coordinates:
    c.rectangle(picture, (x, y), (x+width, y+height), (0, 0, 255), 1)

c.imshow('face_ai', picture)
c.waitKey(0)