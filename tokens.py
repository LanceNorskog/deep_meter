
from __future__ import absolute_import, division, unicode_literals
from itertools import product
from segtok.tokenizer import space_tokenizer

def tokenize(sentence):
  words = space_tokenizer(sentence)
  out = []
  for word in words:
    word = word.lower()
    if word.endswith(","):
      out.append(word[:-1])
      out.append(",")
    else:
      out.append(word)
  if out[-1] == ",":
    out = out[:-1]
  return out

def test(syllables, stresses):
  print(tokenize("the monkeys, they hate me,"))
  print(tokenize2("the monkeys, they hate me,", stresses))
