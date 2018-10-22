import sys
import ast
  
# official one-hot dictionary- pick a smaller number, index from beginning
  
unknown_syllable = '?'
pause_syllble = ','
unknown_encoding = 0
pause_encoding = 1
  
class syllables:
  def __init__(self, size=100000):
    self.syllables = ast.literal_eval(open("blobs/allsyllables.array").readline())
    if size < len(self.syllables):
      self.syllables = self.syllables[0:size]
    self.num_syllables = len(self.syllables)
    self.encodings = {}
    for i in range(self.num_syllables):
      self.encodings[self.syllables[i]] = i

  def get_size(self):
    return self.num_syllables
  
  def get_encoding(self, syll):
    return self.encodings.get(syll, unknown_encoding)
  
  def get_syllable(self, encode):
    if encode < self.num_syllables:
      return self.syllables[encode]
    return unknown_syllable
  
if __name__ == "__main__":
  s = syllables()
  print(s.get_size())
  print(s.get_encoding('?'))
  print(s.get_encoding(','))
  print(s.get_encoding('EY'))
  print(s.get_syllable(47))
