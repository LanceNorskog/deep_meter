
# Class for manipulating syllabized CMU Dictionary
# Matching dicts: syllables & stresses
# syllables: { 'word':[array of syllables], 'word(2)':[]}
# stresses:  { 'word':[array of '1' and '0'] high stress & low or secondary stress
# word: "mugger"
# ['M AH', 'G ER']
# ['1', '0']

import cmudict

class CMUDictSyllables():
  def __init__(self):
    (self.syllables, self.stresses) = cmudict.load_syllables(True)

x = CMUDictSyllables()
print(x.syllables['mugger'])
