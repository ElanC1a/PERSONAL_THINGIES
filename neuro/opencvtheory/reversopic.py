import cv2 as c

def rotation(pic, angle):
    pic_heigt, pic_width=pic.shape[0], pic.shape[1]
    pic_center=(pic_width//2, pic_heigt//2)
    matrix=c.getRotationMatrix2D(pic_center,angle,1)
    return c.warpAffine(pic, matrix, (pic_width, pic_heigt))

picture=c.imread('birdar.jpg')
picture=c.flip(picture,-1)
picture=rotation(picture, 40)
#picture=c.rotate(picture,c.ROTATE_90_CLOCKWISE)
picture=c.resize(picture,(500,600))
c.imshow('r',picture)
c.waitKey(0)