# from https://github.com/joelthchao/keras branch with this item

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import random

import numpy as np
import warnings
import tensorflow as tf
import keras.backend as K
from keras import initializers,regularizers,constraints
from keras.models import Model
from keras.layers import Dense
from keras.engine.base_layer import InputSpec
from keras.engine.topology import Layer
from keras.engine.input_layer import Input

from big_nce import NCE

if __name__ == "__main__":
    # create matching datasets of x*4 width
    def fill(length, input_width, output_width, num_true=1):
      input_data = np.zeros((length, input_width), dtype='float32')
      output_data = np.zeros((length, num_true), dtype='int32')
      for i in range(length):
        for j in range(num_true):
          k = random.randint(0, input_width - 1)
          input_data[i][k] = 1
          output_data[i][j] = min(output_width - 1, int(k * output_width/input_width))
      return input_data, output_data

    # create autoencoder one-hot & labels
    def fill2(length, width, num_true=1):
      data = np.zeros((length, width), dtype='float32')
      labels = np.zeros((length, num_true), dtype='int32')
      for i in range(length):
        for j in range(num_true):
          k = random.randint(0, width - 1)
          data[i][k] = 1
          labels[i][j] = k
      return data, labels

      
    # number of test samples
    num_train = 32*500
    num_test = 32*500
    num_epochs = 50
    # number of classes
    input_width = 2000
    # number of classes
    output_width = 800
    # number of samples for NCE
    num_sampled = 24
    # number of labels
    num_true = 1
    inputs = Input(shape=(input_width,))
    target = Input(shape=(num_true,))  # sparse format, e.g. [1, 3, 2, 6, ...]
    net = Dense(input_width)(inputs)
    net = NCE(units=output_width, num_sampled=4)([net, target])
    model = Model(inputs=[inputs, target], outputs=net)
    model.compile(optimizer='adam', loss=None, metrics=['binary_crossentropy'])
    model.summary()
    #x = np.random.rand(num_train, width)
    train_x, train_y = fill(num_train, input_width, output_width, num_true)
    test_x, test_y = fill(num_test, input_width, output_width, num_true)
    history = model.fit([train_x, train_y], None, epochs=num_epochs)
    for key in history.history.keys():
        print(key)
    predicts = model.predict([test_x, test_y], batch_size=32)
    print(predicts.shape)
    print(predicts[0])
    count = 0
    for test in range(num_test):
      pred = predicts[test]
      indexes = list(np.argsort(pred))
      indexes.reverse()
      print(indexes[0:8], test_y[test][0])
      test_index = -1
      if indexes[0] == test_y[test]:
        count += 1
    print("Found {0} out of {1}".format(count, num_test))
