
from __future__ import absolute_import, division, unicode_literals

import sys
import cmudict
import meter
import tokens

prefix = "test1."
(syllables, stresses) = cmudict.load_syllables(True)

#tokens.test(syllables, stresses)

def deb(x):
  #print(str(x))
  pass

outputs = {}
for name in meter.meters.keys():
  outputs[name] = open(prefix + name, "w")

for line in sys.stdin:
  deb(line)
  words = tokens.tokenize(line)
  possibles = meter.possibles(words, syllables)
  saved = []
  for words in possibles:
    deb(words)
    stressarray = []
    for word in words:
      word = word.lower()
      stress = stresses.get(word, None)
      if stress == None:
        stressarray = []
        break
      else:
        deb("{0},{1}".format(word, stress))
        s = ""
        for st in stress:
          s = s + st
        stressarray.append(s)
      deb(stressarray)
    guesses = meter.meter_loose(stressarray)
    deb(guesses)
    for guess in guesses:
      if not guess in saved:
        outputs[guess].write(line)
        saved.append(guess)

for (name, f) in outputs.items():
  f.close()
