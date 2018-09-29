
import cmudict
import meter

prefix = "test1."
(syllables, stresses) = cmudict.load_syllables(True)

print(stresses['and'])

# for all meters
#  create output file
outputs = {}
for name in meter.meters.keys():
  outputs[name] = open(prefix + name, "w")

# read each line
line = "Houses and rooms are full of perfumes and beets"
words = ["houses", "and", "rooms", "full", "of", "perfumes", "and", "beets"]
stressarray = []
for word in words:
  stress = stresses[word]
  if stress == None:
    stressarray = None
    break
  else:
    print("{0},{1}".format(word, stress))
    s = ""
    for st in stress:
      s = s + st
    stressarray.append(s)

print(stressarray)

guesses = meter.meter_loose(stressarray)
print(guesses)

# for each returned meter
#  append line to meter file

#for name in meter.meter(
