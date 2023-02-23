import cv2 as c
import tensorflow as tf 
import os 

FILE_PATH = 'C:\Program Files\Python310\1_Python_programmes\neuro\cat_or_dog\cat_sad.jpg'
ANIMAL_CATEGORY = ["Cat", "Dog"]

def pic_answer(path):
    IMAGE_SIZE = 50 
    image_array = c.imread('dog.jpg', c.IMREAD_GRAYSCALE)
    print(image_array)

    new_array = c.resize(image_array, (IMAGE_SIZE, IMAGE_SIZE))
    return new_array.reshape(-1, 50, 50, 1)

model_holder = tf.keras.models.load_model("kotopes")
prediction = model_holder.predict([pic_answer(FILE_PATH)])
print(ANIMAL_CATEGORY[int(prediction[0][0])])


