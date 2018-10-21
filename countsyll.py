import collections
import ast
import sys

count = collections.Counter()

for line in sys.stdin:
  text = line.split("\t")[1]
  sylls = ast.literal_eval(text)
  for syll in sylls:
    for s in syll:
      count[s] += 1

commons = count.most_common(2000)

print("length " + str(len(count)))
print(commons[0])
print(commons[-1])
  
print(commons)
x = []
for c in commons:
  x.append(c[0])
print(x)