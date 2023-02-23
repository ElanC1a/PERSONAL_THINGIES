import numpy as np
import cv2 as c
from matplotlib import pyplot as plt
import easyocr as es
import imutils as it

picture=c.imread('rus_car_.png')
picture_gray=c.cvtColor(picture, c.COLOR_BGR2GRAY)

canvas=np.zeros(picture_gray.shape, dtype='uint8')

picture_clear=c.bilateralFilter(picture_gray, 8, 7, 7)

picture_clear=c.Canny(picture_clear, 40, 60)
picture_contours=c.findContours(picture_clear.copy(), c.RETR_TREE, c.CHAIN_APPROX_SIMPLE)

picture_contours=it.grab_contours(picture_contours)
picture_contours=sorted(picture_contours, key=c.contourArea, reverse=True)

position=None

for i in picture_contours:
    group=c.approxPolyDP(i, 4, True)
    if len(group)==4:
        position=group
        break

new_picture=c.drawContours(canvas, [position], 0, 255, -1)
picture_print=c.bitwise_and(picture, picture, mask=canvas)

(x, y)=np.where(canvas==255) 
(x_1, y_1)=(np.min(x), np.min(y))
(x_2, y_2)=(np.max(x), np.max(y))

erased_obj=picture_gray[x_1:x_2, y_1:y_2]

plate_text=es.Reader(['en'])
plate_text=plate_text.readtext(erased_obj)
only_num=plate_text[0][-2]

print(only_num)     

label=c.putText(picture, only_num, (x_1-50, y_2+60), fontFace=c.FONT_HERSHEY_COMPLEX, fontScale=2, color=(0, 0, 255), thickness=2)
label=c.rectangle(picture, (x_1, x_2), (y_1, y_2), color=(0, 0, 255), thickness=1)    #(y_1, y_2-20), (x_2+20, x_1)


#print(position)
plt.imshow(c.cvtColor(label, c.COLOR_BGR2RGB))
plt.show()