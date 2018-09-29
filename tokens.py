
from __future__ import absolute_import, division, unicode_literals
from segtok.tokenizer import space_tokenizer

def tokenize(sentence):
  words = space_tokenizer(sentence)
  out = []
  for word in words:
    if word.endswith(","):
      out.append(word[:-1])
      out.append(",")
    else:
      out.append(word)
  if out[-1] == ",":
    out = out[:-1]
  return out

print(tokenize("the monkeys, they hate me,"))
