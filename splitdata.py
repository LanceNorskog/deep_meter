
import sys
import numpy as np

hashes = []
text = []

for line in sys.stdin:
  hashes = hashes + [hash(line)]
  text.append(line)

#print(hashes[:200])

indices = np.argsort(hashes)
#print(indices[:200])
  
out = open("data.dev", "w")
j = 1 
for i in indices:
  out.write(text[i])
  if j == 5000:
    out.close()
    out = open("data.test", "w")
  if j == 10000:
    out.close()
    out = open("data.train", "w")
  j += 1
out.close()
