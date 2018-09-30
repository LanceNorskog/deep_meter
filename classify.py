
from __future__ import absolute_import, division, unicode_literals

import sys
import cmudict
import meter
import tokens
import string
import collections

prefix = "gutenberg."

(syllables, stresses) = cmudict.load_syllables(True)

# tokens.test(syllables, stresses)

def deb(x):
  #print(str(x) + "\n")
  pass

outputs = {}
for name in meter.meters.keys():
  outputs[name] = open(prefix + name, "w")

failed_list = open("failed_meter.txt", "w")
def fail(line, words):
  failed_list.write(line + "\t" + str(words) + "\n")

total = 0
# found one or more meters
correct = 0
# did not find a meter
failed = 0
# total number of meters guessed
guessed = 0

def filter(line):
  amp = False
  for i in range(len(line)):
    if line[i] == '&':
      amp = True
    elif line[i] == ';' and amp:
      return False
  return True

# one possible set of meters for this line
def do_possible(line, words, poss, saved):
  global guessed
  global failed
  global syllables
  global stresses
  stressarray = meter.getstress(poss, stresses)
  guesses = meter.meter_loose(stressarray)
  deb(line + "->" + str(guesses))
  if len(guesses) == 0:
    failed += 1
    return 
  for guess in guesses:
    if not guess in saved:
      outputs[guess].write(line + "\t" + str(meter.get_syllables(words, syllables)) + "\n")
      saved.append(guess)
      guessed += 1


# all possible meter sets for this line
def do_possibles(line, words, possibles):
  global correct
  global failed
  global syllables
  global stresses
  # incrementally remove pauses if no luck
  if len(possibles) == 0 and words[:-1] == ",":
    words = words[0:-1]
    possibles = meter.possibles(words, syllables)
  while len(possibles) == 0 and "," in words:
    words = list(words)
    words.remove(",")
    possibles = meter.possibles(words, syllables)
  if len(possibles) == 0:
    fail(line, str(words))
    failed += 1
    return
  # only save a line once per guessed meter
  failed_poss = 0
  saved = []
  for poss in possibles:
    do_possible(line, words, poss, saved)
  if len(saved) > 0:
    correct += 1
  else:
    failed += 1
    fail(line, str(possibles[0]))

for line in sys.stdin:
  if not filter(line):
    continue
  total += 1
  line = tokens.clean(line)
  words = tokens.tokenize(line)
  words = tokens.fixtokens(words)
  words = tokens.hyphen(words, syllables)
  possibles = meter.possibles(words, syllables)
  deb(line + " -> " + str(words) + " -> " + str(possibles))
  do_possibles(line, words, possibles)

for (name, f) in outputs.items():
  f.close()

sys.stderr.write("Total: {0}, correct: {1}, guessed {2}, failed: {3}\n".format(total, correct, guessed, failed))
sys.stderr.flush()
