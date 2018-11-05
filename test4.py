from itertools import combinations
import sys

def sub_slices(s):
    for start, end in combinations(range(len(s)), 2):
        yield (s[0:start], s[start:end+1], s[end+1:])

def all_slices(s):
    for (x, y, z) in sub_slices(s):

#def all_slices(s):
#    for 

def get_base(n):
  base = []
  for i in range(n):
    base.append(i)
  return base

def get_slices(n, min, max):
  found = {}
  for (x,y,z) in sub_slices(get_base(n)):
    value = []
    length = 0
    if len(x) >= min and len(x) <= max:
      value.append(x)
      length += len(x)
    if len(y) >= min and len(y) <= max:
      value.append(y)
      length += len(y)
    if len(z) >= min and len(z) <= max:
      value.append(z)
      length += len(z)
    if length == n:
      key = str(value)
      found[key] = value
  return found

possibles = get_slices(6, 2, 4)
print(len(possibles))
print(possibles.keys())