import cv2 as c
import numpy as np

window=np.zeros((400,400,3),dtype='uint8') #uint8 - whole number
#window[]=235,183,52
c.rectangle(window,(0,0),(50,50),(235,183,52),thickness=10)
#c.line
c.circle(window,(90,90),40,(235,183,52),thickness=10)
c.putText(window,'HELLO',(180,180),c.FONT_HERSHEY_DUPLEX,1,(235,183,52))
c.imshow('r',window)
c.waitKey(0)
