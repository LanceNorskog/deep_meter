
from __future__ import absolute_import, division, unicode_literals

import sys
import cmudict
import meter
import tokens

prefix = "test1."
(syllables, stresses) = cmudict.load_syllables(True)

outputs = {}
for name in meter.meters.keys():
  outputs[name] = open(prefix + name, "w")

for line in sys.stdin:
  words = tokens.tokenize(line)
  stressarray = []
  for word in words:
    word = word.lower()
    stress = stresses.get(word, None)
    if stress == None:
      stressarray = []
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

for (name, f) in outputs.items():
  f.close()
