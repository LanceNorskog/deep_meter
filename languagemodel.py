# language models

class NoModel:
  def __init__(self):
    pass

  def getUnigramProb(self, word):
    return 1.0

  def getBigramProb(self, word, word2):
    return 1.0

  def getNext(self, word):
    return []
