import sys
import ast
  
# 2000 most common syllables, in order
# official one-hot dictionary- pick a smaller number, index from beginning
  
  
# map of syll to dict
syll_to_encode = {}
encode_to_syll = []

unknown_syll = '?'
unknown_encode = -1
  
class syllables:
  def __init__(self):
    self.syllables = ast.literal_eval(open("blobs/allsyllables.array").readline())
    print(len(self.syllables))
    print(self.syllables[0:5])

  def set_size(size):
    global encode_to_syll
    global syll_to_encode
    encode_to_syll = common_2000[0:size]
    syll_to_encode = {}
    for i in range(size):
      syll_to_encode[encode_to_syll[i]] = i
    sys.stderr.write(str(encode_to_syll) + "\n")
  
  def get_size():
    global encode_to_syll
    return len(encode_to_syll)
  
  def get_encoding(syll):
    global syll_to_encode
    return syll_to_encode.get(syll, unknown_encode)
  
  def get_syllable(encode):
    global encode_to_syll
    if encode < len(encode_to_syll):
      return encode_to_syll[encode]
    else:
      return unknown_syll
  
  
s = syllables()
