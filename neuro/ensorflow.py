import keras as K
import numpy as np

input_var=np.expand_dims(np.array([0.2,0.4,1.0]),axis=1)
output_var=np.expand_dims(np.array([0.1,0.3,1.0]),axis=1)

model=K.models.Sequential()
model.add(K.layers.Dense(units=1,activation='linear'))
model.compile(loss='mse',optimizer='sgd')

tutorial=model.fit(x=input_var,y=output_var,epochs=100)

answer=model.predict([0.9])
print(answer)