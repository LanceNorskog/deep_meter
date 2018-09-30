
from __future__ import absolute_import, division, unicode_literals

import sys
import cmudict
import meter
import tokens

prefix = "gutenberg."

(syllables, stresses) = cmudict.load_syllables(True)

#tokens.test(syllables, stresses)

def deb(x):
  print(str(x) + "\n")
  pass

outputs = {}
for name in meter.meters.keys():
  outputs[name] = open(prefix + name, "w")

failed_list = open("failed_meter.txt", "w")
def fail(line, words):
  failed_list.write(line + "\t" + str(words) + "\n")

total = 0
correct = 0
guessed = 0
failed = 0

for line in sys.stdin:
  total += 1
  line = tokens.clean(line)
  words = tokens.tokenize(line)
  words = tokens.fixtokens(words)
  words = tokens.hyphen(words, syllables)
  deb(line + " -> " + str(words))
  possibles = meter.possibles(words, syllables)
  # incrementally remove pauses if no luck
  if len(possibles) == 0 and words[:-1] == ",":
    words = words[0:-1]
    possibles = meter.possibles(words, syllables)
  while len(possibles) == 0 and "," in words:
    words.remove(",")
    possibles = meter.possibles(words, syllables)
  if len(possibles) == 0:
    fail(line, str(words))
    failed += 1
    continue
  # only save a line once per guessed meter
  saved = [] 
  last_failed = None
  for words in possibles:
    #deb(words)
    stressarray = meter.getstress(words, stresses)
    guesses = meter.meter_loose(stressarray)
    #deb(line + "->" + str(guesses))
    if len(guesses) == 0:
      failed += 1
      if line != last_failed:
        fail(line, str(words))
        last_failed = line
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
