import cv2 as c
import numpy as np

picture=c.imread('carddeck.jpg')
canvas=np.zeros(picture.shape, dtype='uint8')

picture=c.cvtColor(picture, c.COLOR_BGR2GRAY)
picture=c.GaussianBlur(picture, (5,7), 0)

picture=c.Canny(picture, 255, 40)

matrix_id, hierarchy=c.findContours(picture, c.RETR_LIST, c.CHAIN_APPROX_SIMPLE)

c.drawContours(canvas, matrix_id, -1, (23, 7, 245), 1)

c.imshow('card', canvas)
c.waitKey(0)
