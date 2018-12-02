# Manage Transfer Learning models

# boilerplate from base notebook
import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import re
import seaborn as sns
import keras.layers as layers
from keras.models import Model
from keras import backend as K
from keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.optimizers import Nadam, Adam
import gc
from google.colab import files
from google.colab import drive

import pickle
np.random.seed(10)

# Squid model has a separate brain in each tentacle

def new_squid_model(embed_size, num_symbols, num_syllables, optimizer='adam', dropout=0.5):
    input_embeddings = layers.Input(shape=(embed_size,), dtype=tf.float32, name='Input')
    dense_input = layers.Dropout(dropout)(input_embeddings)
    dense = layers.Dense(1024, activation='relu', name='Convoluted')(dense_input)
    dense = layers.Dropout(dropout)(dense)
    dense = layers.Dense(2048, activation='relu', name='Midway')(dense)
    squid_names_array = []
    pred_array = []
    loss_array = []
    names_array = []
    for i in range(num_symbols):
      squid = layers.Dropout(dropout)(dense)
      squid = layers.Dense(256, activation='relu', name='Squid'+str(i))(squid)
      squid = layers.Dropout(dropout)(squid)
      name = 'Flatout'+str(i)
      pred_array.append(layers.Dense(num_syllables, activation='softmax', name=name)(squid))
      loss_array.append('categorical_crossentropy')
      names_array.append(name)
    model = Model(inputs=input_embeddings, outputs=pred_array)
    model.compile(loss=loss_array, 
                  optimizer=optimizer, 
                  metrics=['categorical_accuracy'])
    return model

def save_squid_model(model):
    model.save_weights('./model_squid.h5')


def load_squid_model(model):
    model.load_weights('./model_squid.h5')  

def remove_squid_model():
    os.remove('./model_squid.h5')

# Joel Chao
def pop_layer(model):
def pop_layer(model):
    if not model.outputs:
        raise Exception('Sequential model cannot be popped: model is empty.')

    model.layers.pop()
    if not model.layers:
        model.outputs = []
        model.inbound_nodes = []
        model.outbound_nodes = []
    else:
        model.layers[-1].outbound_nodes = []
        model.outputs = [model.layers[-1].output]
    model.built = False

