# Keras generator for text + sylls

# Read text lines, syllable-ize them.
# Return in batches to main loop
# Don't use 'yield', it does not multi-process well.

# Because of size concerns, tokenize each line of text on each epoch

# based on: https://stanford.edu/~shervine/blog/keras-how-to-generate-data-on-the-fly

from random import shuffle
import numpy as np
import os
import cmudict
import tokens

# base test set
DIR='/content/data'
DIR='./junk'
FILE_LINES=20000
LINES=3085117

# encode one line, if all syllables are in syllable dictionary
def encode(line, cmudict, syll_mgr):
    line = tokens.clean(line)
    words = tokens.tokenize(line)
    words = tokens.fixtokens(words)
    words = tokens.hyphen(words, cmudict.syll_dict)
    encs = []
    for w in words:
         sylls = cmudict.get_sylls(word)
         for syll in sylls:
             enc = syll_mgr.get_encoding(syll)
             if enc == syll_mgr.unknown_enc:
                 return None
             encs.append(syll)
    labels = [0] * syll_mgr.get_size()
    for enc in encs:
        labels[enc] = 1
    return labels


class DataGenerator(keras.utils.Sequence):
    'Generates data for Keras'
    def __init__(self, dir=DIR, file_length=FILE_LINES, num_lines=LINES, batch_size=32, shuffle=True):
        'Initialization'
        self.dir = dir
        self.list_IDs = []
        for file in os.listdir(dir):
            self.list_IDs.append(dir + '/' + file)
        self.indexes = [1] * len(self.list_IDs)
        for i in range(len(self.list_IDs)):
            self.indexes[i] = i
        self.file_lines = file_lines
        self.num_lines = num_lines
        self.batch_size = batch_size
        self.syll_mgr = syllables.syllables()
        self.n_classes = self.syll_mgr.get_size()
        self.shuffle = shuffle
        self.on_epoch_end()
        self.cmudict = cmudict.CMUDict()

    def __len__(self):
        'Denotes the number of batches per epoch'
        return len(self.list_IDs)

    def __getitem__(self, index):
        'Generate one batch of data'

        # read text & syllabize
        lines = os.open(self.list_IDs[index], "r").readlines()
        text_array = [] # one per accepted line
        labels_array = [] # one per multi-label onehot
        for line in lines:
            labels = encode_line(line, self.cmudict, self.syll_mgr)
            if labels != None:
                text_array.append(line)
                labels_array.append(labels)

        # Generate data
        return np.array(text_array), np.array(labels_array)

    def on_epoch_end(self):
        'Updates indexes after each epoch'
        self.indexes = np.arange(len(self.list_IDs))
        if self.shuffle == True:
            np.random.shuffle(self.indexes)

if __name__ == "__main__":
    gen = DataGenerator()
    print('Num batches: {}'.format(gen.__len__))
    (text, labels) = gen.__getitem__(0)
    print('Text: '.format(text.shape))
    print('Labels: '.format(labels.shape))
