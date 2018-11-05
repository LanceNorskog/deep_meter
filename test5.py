from itertools import combinations
import sys

# syllables range from 2 to 6 phonemes long

def sub_slices2(s):
    for start, end in combinations(range(len(s)), 2):
        yield (s[0:start], s[start:end+1], s[end+1:])

def sub_slices3(s):
    for start, mid, end in combinations(range(len(s)), 3):
        yield (s[0:start], s[start:mid+1], s[mid+1:end+1], s[end+1:])

def sub_slices4(s):
    for start, mid1, mid2, end in combinations(range(len(s)), 4):
        yield (s[0:start], s[start:mid+1], s[mid+1:mid2+1], s[mid2+1:end+1], s[end+1:])

def sub_slices5(s):
    for start, mid1, mid2, mid3, end in combinations(range(len(s)), 5):
        yield (s[0:start], s[start:mid+1], s[mid1+1:mid2+1], s[mid2+1:mid3+1], s[mid3+1:end+1], s[end+1:])

print(sub_slices2([1,2,3,4,5,6]))
print(sub_slices3([1,2,3,4,5,6]))
print(sub_slices4([1,2,3,4,5,6]))
print(sub_slices5([1,2,3,4,5,6]))

sys.exit(0)

# possible combinations of slices, redundancies
def all_slices(s):
    all = []
    for (x, y, z) in sub_slices(s):
      x = list(x)
      y = list(y)
      z = list(z)
      if len(x) > 2:
         for (a, b, c) in sub_slices(x):
           

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
