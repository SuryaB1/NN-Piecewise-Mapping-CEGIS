import tensorflow as tf
from tensorflow import keras
import numpy as np

# if in concave pentagon, 1, otherwise 0
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=5, activation='relu', input_shape=(2,), # y<0, x>-5, x<-1, y>x or y>-x-6
                          kernel_initializer=tf.constant_initializer([[0.0, 1.0, -1.0, -1.0, 1.0], 
                                                                      [-1.0, 0.0, 0.0, 1.0, 1.0]]),
                          bias_initializer=tf.constant_initializer([0.0, 5.0, -1.0, 0.0, 6.0])),

    # Convert to 0 or 1
    tf.keras.layers.Dense(units=10, activation='relu', # convert difference to 2D vector with diff and diff - 1
                          kernel_initializer=tf.constant_initializer([[1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
                                                                      [0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
                                                                      [0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0], 
                                                                      [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0], 
                                                                      [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0]]),
                          bias_initializer=tf.constant_initializer([0.0, -1.0, 0.0, -1.0, 0.0, -1.0, 0.0, -1.0, 0.0, -1.0])),
    tf.keras.layers.Dense(units=5, activation='relu',
                          kernel_initializer=tf.constant_initializer([[1.0, 0.0, 0.0, 0.0, 0.0], 
                                                                      [-1.0, 0.0, 0.0, 0.0, 0.0], 
                                                                      [0.0, 1.0, 0.0, 0.0, 0.0], 
                                                                      [0.0, -1.0, 0.0, 0.0, 0.0], 
                                                                      [0.0, 0.0, 1.0, 0.0, 0.0], 
                                                                      [0.0, 0.0, -1.0, 0.0, 0.0], 
                                                                      [0.0, 0.0, 0.0, 1.0, 0.0], 
                                                                      [0.0, 0.0, 0.0, -1.0, 0.0], 
                                                                      [0.0, 0.0, 0.0, 0.0, 1.0], 
                                                                      [0.0, 0.0, 0.0, 0.0, -1.0]]),
                          bias_initializer=tf.constant_initializer([0.0, 0.0, 0.0, 0.0, 0.0])),

    tf.keras.layers.Dense(units=2, activation='relu', # one neuron for y<0, x>-5, x<-1, y>x, other for y<0, x>-5, x<-1, y<-x-6
                          kernel_initializer=tf.constant_initializer([[1.0, 1.0], 
                                                                      [1.0, 1.0], 
                                                                      [1.0, 1.0], 
                                                                      [1.0, 0.0], 
                                                                      [0.0, 1.0]]),
                          bias_initializer=tf.constant_initializer([-3.0, -3.0])),
    tf.keras.layers.Dense(units=1, activation='relu',
                          kernel_initializer=tf.constant_initializer([[1.0], [1.0]]),
                          bias_initializer=tf.constant_initializer([0.0])),

    # Convert to 0 or 1
    tf.keras.layers.Dense(units=2, activation='relu', # convert difference to 2D vector with diff and diff - 1
                          kernel_initializer=tf.constant_initializer([[1.0, 1.0]]),
                          bias_initializer=tf.constant_initializer([0.0, -1.0])),
    tf.keras.layers.Dense(units=1, activation='relu',
                          kernel_initializer=tf.constant_initializer([[1.0], [-1.0]]),
                          bias_initializer=tf.constant_initializer([0.0])),
])

model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])

input = np.array([[-4, -5]])
output = model.predict(input)
print(output)

tf.saved_model.save(model, '../saved_models/concave-poly_classif_nnet')