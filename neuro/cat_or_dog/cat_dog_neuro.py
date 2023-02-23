import pickle
import cv2 as c
import numpy as np
import os
import random as rnd
import matplotlib.pyplot as plt
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout, Activation, MaxPooling2D, Conv2D
from keras.datasets import cifar10 
import tqdm
import tqdm.auto
tqdm.tqdm = tqdm.auto.tqdm  


FILE_PATH = "C:/Program Files/Python310/1_Python_programmes/neuro/cat_or_dog/PetImages"
ANIMAL_CATEGORY = ["Cat", "Dog"]
IMAGE_SIZE = 50 

train_data = []

def create_train_data():
    for animal in ANIMAL_CATEGORY:
        path = os.path.join(FILE_PATH, animal)
        index_assign = ANIMAL_CATEGORY.index(animal) # 0 - cat; 1 - dog
        for image in os.listdir(path):
            try:
                image_massiv = c.imread(os.path.join(path, image), c.IMREAD_GRAYSCALE)
                new_image = c.resize(image_massiv, (IMAGE_SIZE, IMAGE_SIZE))
                train_data.append([new_image, index_assign])

            except:
                pass

create_train_data()
print(len(train_data))

rnd.shuffle(train_data) #чтобы не переучить

pic_only = []
ans_only = []

for image, index in train_data:
    pic_only.append(image)
    ans_only.append(index)  #index i.e: cat - 0 or dog - 1 

pic_only = np.array(pic_only).reshape(-1, 50, 50, 1) # -1 - auto find amount of rows, 1 - amount of layers (in our case grayscale - 1 )

pickle_out = open("x.pickle", "wb")
pickle.dump(pic_only, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle", "wb")
pickle.dump(ans_only, pickle_out)
pickle_out.close()

pickle_in = open("x.pickle", "rb")
pic_only = pickle.load(pickle_in)

pickle_in = open("y.pickle", "rb")
ans_only = pickle.load(pickle_in)

pic_only = np.array(pic_only/255.0)     #[253, 234, 30,] --> reason we no need Flatten, since we already have flatten list
ans_only = np.array(ans_only)

model = Sequential()
model.add(Conv2D(64, 3, input_shape=pic_only.shape[1:])) ###??? sprosit   3 - шаг по которому он проходит лист | pic_only - 
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=2))

model.add(Conv2D(64, 3))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=2))

model.add(Conv2D(64, 3))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=2))

model.add(Conv2D(64, 3))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=2))

model.add(Flatten())
model.add(Dense(1))
model.add(Activation("sigmoid"))

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

model.fit(pic_only, ans_only, batch_size=32, epochs=9, validation_split=0.2)
model.save("kotopes")