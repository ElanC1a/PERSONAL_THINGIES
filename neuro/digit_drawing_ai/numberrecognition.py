import tensorflow as tf
import tensorflow_datasets as tm
import matplotlib.pyplot as plt
from keras.datasets import mnist
import numpy as np
import tqdm
import tqdm.auto
tqdm.tqdm = tqdm.auto.tqdm  

from keras.preprocessing import image

#setup of dataset
(train_picture, train_answer_picture),(test_picture,test_answer_picture)=mnist.load_data()

# train_picture=train_picture.reshape(train_picture.shape[0],28,28,1)       #?????
# test_picture=test_picture.reshape(test_picture.shape[0],28,28,1)          #?????

# train_picture=tf.cast((train_picture/255), tf.float32)                #?????
# test_picture=test_picture/255             #?????

train_picture=tf.keras.utils.normalize(train_picture,axis=1)    #?????
test_picture=tf.keras.utils.normalize(test_picture,axis=1)      #?????

#model
model=tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28,1)),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    # tf.keras.layers.Dropout(0.8),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax),
])

# print(model.summary())

#[0,0,0,1,0,0,0,0,0,0]
train_answer_picture_vec=tf.keras.utils.to_categorical(train_answer_picture,10)
test_answer_picture_vec=tf.keras.utils.to_categorical(test_answer_picture,10)

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(train_picture, train_answer_picture_vec, epochs=2, batch_size=32)

#accuracy
model.evaluate(test_picture, test_answer_picture_vec)

#choosing 1 pic

# odin=10
# dwa=np.expand_dims(test_picture[odin],axis=0)
# result=model.predict(dwa)
# print(result)
# print(np.argmax(result))

# plt.figure(figsize=(6,5))
# plt.imshow(test_picture[odin],cmap=plt.cm.binary)
# plt.xlabel(np.argmax(result))
# plt.show()

model.save('digit_recog.h5')