import collections

# load cmudict-syllables
# dict {word -> [syllable list]

cmudict = "/Users/l0n008k/open/data/cmudict_0.6.syllablized.txt"
def load_syllables(do_stresses):
  x = 0
  with open(cmudict, "r") as ins:
    syllables = {}
    stresses = {}
    for line in ins:
      if line.startswith("#"):
        continue
      #print(line)
      words = line.split(" ")
      key = words[0]
      rest = words[2:]
      syllarray = []
      stressarray = []
      syll = ""
      last = ""
      for arpa in rest:
        if arpa.endswith("\n"):
          arpa = arpa[:-1]
        if arpa.endswith("0"):
          stressarray.append("0")
          arpa = arpa[:-1]
        elif arpa.endswith("1") or arpa.endswith("2"):
          stressarray.append("1")
          arpa = arpa[:-1]
        if arpa == "-":
          syllarray.append(syll)
          syll = ""
        elif last == "-":
          syll = arpa
        elif syll == "":
          syll = arpa
        else:
          syll = syll + " " + arpa
        last = arpa
      syllarray.append(syll)
      #print(key + str(syllarray) + str(stressarray))
      syllables[key] = syllarray
      if do_stresses:
        stresses[key] = stressarray
      x = x + 1
      #if x == 100:
      #  break
  return (syllables, stresses)

(syllables, stresses) = load_syllables(True)
print(syllables['ZERO'])
print(stresses['ZERO'])

count = collections.Counter()
for word in syllables.keys():
  for syll in syllables[word]:
    count[syll] += 1

print(count.most_common(300))
print(len(count))
