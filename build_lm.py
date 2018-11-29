# load digested corpus, build language model object, and pickle

import sys
import pickle
from ast import literal_eval

import languagemodel
import cmudict
import tokens


sm = languagemodel.SyllableModel()
cmudict = cmudict.CMUDict()

print('Starting')
count = 0
for line in sys.stdin:
    parts = line.split('\t')
    text = parts[0]
    syllables = literal_eval(parts[1][:-1])  # newline
    text = tokens.clean(text)
    words = tokens.tokenize(text)
    words = tokens.fixtokens(words)
    words = tokens.hyphen(words, cmudict.syll_dict)
    clean = []
    for word in words:
        if word != ',':
            clean.append(word)
    count += 1
    if len(clean) != len(syllables):
        print("Line #: " + str(count))
        print(clean)
        print(syllables)
        continue
    for i in range(len(clean)):
        sm.addWord(clean[i], syllables[i])

print('Saving')
languagemodel.saveModel(sm)
    