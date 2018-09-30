
from __future__ import absolute_import, division, unicode_literals
from itertools import product
from segtok.tokenizer import space_tokenizer, web_tokenizer
import num2words

def tokenize1(sentence):
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

# scrub some dirt out
def clean(sentence):
  sentence = sentence.replace("\\","")
  sentence = sentence.replace("'","")
  sentence = sentence.replace("`","")
  return sentence

def tokenize(sentence):
  words = web_tokenizer(sentence)
  out = []
  for word in words:
    word = word.lower()
    if word != "_":
      out.append(word)
  return out

# dot,comma, semi become optional. 
# numbers, cmudict only has spelled-out words
def fixtokens(words):
  out = []
  for word in words:
    pass

def test(syllables, stresses):
  print(tokenize("the monkeys, they hate me,"))
  print(tokenize2("the monkeys, they hate me,", stresses))
