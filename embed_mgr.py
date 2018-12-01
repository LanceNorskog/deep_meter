# Keras model manager

# boilerplate from base notebook
import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import numpy as np
import os
from keras import backend as K

import pickle
np.random.seed(10)

class use_mgr:
    def __init__(self, module_url="https://tfhub.dev/google/universal-sentence-encoder-large/3"):
        self.embed = None
        self.embed_size = 0

    def load_use(self:
        # Reduce logging output.
        tf.logging.set_verbosity(tf.logging.ERROR)
        # Import the Universal Sentence Encoder's TF Hub module
        self.embed = hub.Module(module_url)
        # important?
        self.embed_size = embed.get_output_info_dict()['default'].get_shape()[1].value
        return self.embed_size

    def run_use(text_array):
        with tf.Session() as session:
          session.run([tf.global_variables_initializer(), tf.tables_initializer()])
          embeddings = session.run(self.embed(text_array))
        return embeddings

    def unload_use():
        del self.embed

