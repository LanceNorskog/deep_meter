
from __future__ import absolute_import, division, unicode_literals

import sys
import cmudict
import meter
from segtok.tokenizer import space_tokenizer

prefix = "test1."
(syllables, stresses) = cmudict.load_syllables(True)

#print(stresses['and'])

# for all meters
#  create output file
outputs = {}
for name in meter.meters.keys():
  outputs[name] = open(prefix + name, "w")

# read each line
for line in sys.stdin:
  #line = "Houses and rooms full of perfumes and beets"
  #words = ["houses", "and", "rooms", "full", "of", "perfumes", "and", "beets"]
  words = space_tokenizer(line)
  #print(words)
  stressarray = []
  for word in words:
    word = word.lower()
    #print(word)
    stress = stresses[word]
    if stress == None:
      stressarray = None
      break
    else:
      #print("{0},{1}".format(word, stress))
      s = ""
      for st in stress:
        s = s + st
      stressarray.append(s)
  #print(stressarray)
  guesses = meter.meter_loose(stressarray)
  #print(guesses)
# for each returned meter
#  append line to meter file
  for guess in guesses:
    #f = outputs[guess]
    #print(type(f))
    #f.write(line)
    outputs[guess].write(line)
  break
for (name, f) in outputs.items():
  f.close()
