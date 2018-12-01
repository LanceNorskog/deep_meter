# Keras model manager

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

tf_hub_use_module = "https://tfhub.dev/google/universal-sentence-encoder-large/3"
embed = None
embed_size = 0

def load_use(module_url="https://tfhub.dev/google/universal-sentence-encoder-large/3"):
    # Import the Universal Sentence Encoder's TF Hub module
    embed = hub.Module(module_url)
    # important?
    embed_size = embed.get_output_info_dict()['default'].get_shape()[1].value

    # Reduce logging output.
    tf.logging.set_verbosity(tf.logging.ERROR)

def run_use(text_array):
    with tf.Session() as session:
      session.run([tf.global_variables_initializer(), tf.tables_initializer()])
      embeddings = session.run(embed(text_array))
    return embeddings

def unload_use():
    K.clear_session()
    del embed

