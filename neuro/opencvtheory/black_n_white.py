import cv2 as c

image=c.imread('fat_yo.jpg')
image=c.resize(image,(image.shape[1],image.shape[0]))

#image=c.cvtColor(image,c.COLOR_BGR2GRAY)
r,g,b=c.split(image)

#image=c.Canny(image,40,40)

image=c.merge([])
c.imshow('image', image)
c.waitKey(0)
