import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import math
import tensorflow_datasets as tm
import tqdm
import tqdm.auto
tqdm.tqdm = tqdm.auto.tqdm  

#setup of dataset
data_set, meta_data=tm.load('fashion_mnist',as_supervised=True, with_info=True)
train_data, test_data=data_set['train'], data_set['test']
class_names = ["T-shirt/top",
  "Trouser",
  "Pullover",
  "Dress",
  "Coat",
  "Sandal",
  "Shirt",
  "Sneaker",
  "Bag",
  "Ankle boot"
]
amount_oftrain=meta_data.splits['train'].num_examples
amount_oftest=meta_data.splits['test'].num_examples
print(amount_oftrain,amount_oftest)

#picture/ diagram
def normalization(picture,label):
  picture=tf.cast(picture, tf.float32)
  picture/=255
  return picture, label

train_data=train_data.map(normalization)
test_data=test_data.map(normalization)

#testing 1 pic
# for picture, label in train_data.take(1):
#   break
# picture=picture.numpy().reshape((28,28))
# plt.figure(figsize=(10,10))
# plt.imshow(picture,cmap=plt.cm.binary)
# plt.xlabel(class_names[label])
# plt.show()

#model
model=tf.keras.Sequential([
  tf.keras.layers.Flatten(input_shape=(28,28,1)),
  tf.keras.layers.Dense(128,activation=tf.nn.relu),   #relu - ? return to it
  tf.keras.layers.Dense(10,activation=tf.nn.softmax)
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

#batch
BATCH_SIZE=32
train_data=train_data.repeat().shuffle(amount_oftrain).batch(BATCH_SIZE)
test_data=test_data.batch(BATCH_SIZE)

#model training
model.fit(train_data, epochs=5, steps_per_epoch=amount_oftrain/BATCH_SIZE)       #1 875

#accuracy
test_loss, test_accuracy=model.evaluate(train_data, steps=amount_oftest/BATCH_SIZE)
print('\nTest accuracy:', test_accuracy)

#choosing 1 pic
for picture, label in test_data.take(1):
  picture=picture.numpy() #!!! list
  label=label.numpy()
  predictions=model.predict(picture)

print(predictions[0])
print(np.argmax(predictions[0]))
print(label[0])

def print_picture(index, predictions, right_answer, picture):
  predictions, right_answer, picture=predictions[index], right_answer[index], picture[index]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  plt.imshow(picture, cmap=plt.cm.binary)
  ai_prediction=np.argmax(predictions)
  plt.xlabel('{0},{1}'.format(class_names[ai_prediction], class_names[right_answer]))

#index=2
#plt.figure(figsize=(8,3))
# print_picture(index, predictions,label,picture)

num_rows = 5
num_cols = 6
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  print_picture(i, predictions,label,picture)
plt.tight_layout()
plt.show()