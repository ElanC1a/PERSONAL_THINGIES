import cv2 as c
import numpy as np
picture=c.imread('roadpov.jpg')
canvas=np.zeros(picture.shape, dtype='uint8')

picture=c.cvtColor(picture, c.COLOR_BGR2GRAY)
picture=c.GaussianBlur(picture, (5,7), 0)
picture=c.Canny(picture, 255, 0)
matrix_conturing, hierarchy=c.findContours(picture, c.RETR_LIST, c.CHAIN_APPROX_NONE)


c.drawContours(canvas, matrix_conturing, -1, (180, 0, 99), 1)

c.imshow('r', canvas)
c.waitKey(0)