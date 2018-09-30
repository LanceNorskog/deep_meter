
from __future__ import absolute_import, division, unicode_literals

import sys
import cmudict
import meter
import tokens

prefix = "gutenberg."

(syllables, stresses) = cmudict.load_syllables(True)

#tokens.test(syllables, stresses)

def deb(x):
  #print(str(x))
  pass

outputs = {}
for name in meter.meters.keys():
  outputs[name] = open(prefix + name, "w")

failed_list = open("failed_meter.txt", "w")

total = 0
correct = 0
guessed = 0
failed = 0

for line in sys.stdin:
  total += 1
  line = tokens.clean(line)
  deb(line)
  words = tokens.tokenize(line)
  words = tokens.fixtokens(words)
  possibles = meter.possibles(words, syllables)
  if len(possibles) == 0:
    failed_list.write(line + "\t" + str(words))
    failed += 1
    continue
  # only save a line once per guessed meter
  saved = [] 
  for words in possibles:
    #deb(words)
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
    if len(guesses) == 0:
      failed_list.write(line)
      failed += 1
      continue
    for guess in guesses:
      if not guess in saved:
        outputs[guess].write(line)
        saved.append(guess)
        guessed += 1
  correct += 1

for (name, f) in outputs.items():
  f.close()

sys.stderr.write("Total: {0}, correct: {1}, guessed {2}, failed: {3}\n".format(total, correct, guessed, failed))
sys.stderr.flush()
