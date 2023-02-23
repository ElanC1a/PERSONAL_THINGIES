import cv2 as c 

# image=c.imread('fat_yo.jpg')
# c.imshow('picture',image)
# c.waitKey(0)

video=c.VideoCapture('rick_roll.mp4')
while False:
    val, frame=video.read()
    c.imshow('video',frame)
    if c.waitKey(28) & 0xFF==ord('q'):
        break
    #add sound
    
camera=c.VideoCapture(0)
camera.set(3,600)
camera.set(4,800)
while True:
    val, frame=camera.read()
    c.imshow('camera',frame)
    if c.waitKey(1) & 0xFF==ord('q'):
        break
