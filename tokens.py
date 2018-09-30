
from __future__ import absolute_import, division, unicode_literals
from itertools import product
from segtok.tokenizer import space_tokenizer, web_tokenizer
import num2words
import string

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

# dot, comma, semi become comma 
# numbers, cmudict only has spelled-out words
# maybe "pine-trees" should be a "10" stress, but create ["1", "1"]
def fixtokens(words):
  out = []
  for word in words:
    if word == "," or word == ";" or word == ".":
      out.append(',')
    elif len(word) == 0 or string.punctuation.find(word[0]) > -1:
      pass
    elif word.find("-"):
      subwords = word.split("-")
      for sub in subwords:
        out.append(sub)
    else:
      out.append(word)
  out2 = []
  for word in out:
    if word.endswith("."):
      out2.append(word[:-1])
      out2.append(",")
    else:
      out2.append(word)
  return out2

# return array of tokenized wordsets for a number
def digitize(number):
  pass
      
def test(syllables, stresses):
  print(tokenize("the monkeys, they hate me,"))
  print(tokenize2("the monkeys, they hate me,", stresses))
