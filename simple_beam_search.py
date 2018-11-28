# stolen from https://machinelearningmastery.com/beam-search-decoder-natural-language-processing/

from math import log
import numpy as np
import sys
from languagemodel import NoModel

# beam search
def beam_search_decoder(data, k):
    sequences = [[list(), 1.0]]
    # walk over each step in sequence
    for row in data:
        all_candidates = list()
        # expand each current candidate
        for i in range(len(sequences)):
            seq, score = sequences[i]
            for j in range(len(row)):
                candidate = [seq + [j], score * row[j]]
                all_candidates.append(candidate)
        # order all candidates by score
        ordered = sorted(all_candidates, key=lambda tup:tup[1])
        # select k best
        sequences = ordered[:k]
    return sequences

# beam search
def word_beam_search_decoder(data, k, lm):
    sequences = [[list(), 1.0]]
    # walk over each step in sequence
    for row in data:
        all_candidates = list()
        # expand each current candidate
        for i in range(len(sequences)):
            seq, score = sequences[i]
            numWords = len(row)
            for j in range(numWords):
                wscore = score
                wscore *= row[j]
                scale = lm.getUnigramProb(row[0])
                next = lm.getNext(row[j])
                if len(next) > 0:
                    for word in next:
                        scale += lm.getBigramProb(row[j-1], row[j])
                else:
                    scale += lm.getUnigramProb(row[j])
                if numWords > 1:
                    scale ** (1/(numWords+1))
                candidate = [seq + [j], wscore * scale]
                all_candidates.append(candidate)
        # order all candidates by score
        ordered = sorted(all_candidates, key=lambda tup:tup[1])
        # select k best
        sequences = ordered[:k]
    return sequences

if __name__ == "__main__":
    # define a sequence of 10 words over a vocab of 5 words
    data = np.random.random((10,5))
    data = np.array(data)
    # decode sequence
    result = beam_search_decoder(data, 7)
    print(result)
    result2 = word_beam_search_decoder(data, 7, NoModel())
    print(result2)
    for i in range(len(result)):
      for j in range(len(result[0])):
        if result[i][0][j] != result2[i][0][j]:
          print("[{}][{}] -> ({}, {})".format(i, j, result[i][j], result2[i][j]))
          print('Fail!')
          sys.exit(1)
