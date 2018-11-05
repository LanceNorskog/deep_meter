#Knuth's "Algorithm U", from stackoverflow
# https://codereview.stackexchange.com/questions/1526/finding-all-k-subset-partitions

import utils
import itertools
def neclusters(l, K):
    for splits in itertools.combinations(range(len(l) - 1), K - 1):
        # splits need to be offset by 1, and padded
        splits = [0] + [s + 1 for s in splits] + [None]
        yield [l[s:e] for s, e in zip(splits, splits[1:])]

def neclusters2(l, K):
    for splits in itertools.combinations(range(len(l) - 1), K - 1):
        # splits need to be offset by 1, and padded
        print('')
        splits = [0] + [s + 1 for s in splits] + [None]
        for s, e in zip(splits, splits[1:]):
            yield (s,e)

for (s,e) in neclusters2([1,2,3,4,5],3):
  print("{0} -> {1}".format(s, e))
  if e == None:
    print('')

def walk(s, n):
  out = []
  for l in neclusters(s, n):
    out.append(list(l))
  return out

def checkordered(l):
  val = -1
  for x in utils.flatten(l):
    if val + 1 == x:
      val = x
    else:
      return False
  return True

def checklength(lli, min, max):
  for li in lli:
    if not(len(li) >= min and len(li) <= max):
      return False
  return True
    
def walkordered0(s, n):
  out = []
  for l in neclusters(s, n):
    l = list(l)
    if checkordered(l) and checklength(l, 2, 6):
      out.append(l)
  return out

def walkordered(s, n):
  print('')
  out = []
  for l in neclusters(s, n):
    l = list(l)
    if checkordered(l) and checklength(l, 2, 6):
       print(l)

if __name__ == "__main__":
  #print(walk([0,1,2,3],2))
  #walkordered([0,1,2],2)
  #print(walkordered([0,1,2,3],3))
  #print(walkordered([0,1,2,3,4,5,6,7],2))
  #walkordered(list(range(10)),4)
  #walkordered(list(range(15)),4)
  walkordered(list(range(30)),10)
  walkordered(list(range(40)),10)
  #print(walkordered(list(range(15)),3))
  #print(walkordered(list(range(15)),4))
  #print(walkordered(list(range(15)),5))
  #print(walkordered(list(range(15)),6))
