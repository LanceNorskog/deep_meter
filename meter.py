import stringdist
from itertools import product

# meter from cmudict: ['0', '10', '10']

meters = {"iambic_pentameter": "0101010101", "hiawatha": "10101010"}

notfound_list = open("word_not_found.txt", "w")

# all possible variations of cmudict for word
def possibles_word(word, worddict):
  position = []
  if worddict.get(word, None) == None:
    notfound_list.write(word + "\n")
  for suffix in [ '', '(2)', '(3)', '(4)', '(5)', '(6)' ]:
    check = word + suffix
    #print("{0},{1}".format(check, str(wordlist.get(check, "none"))))
    if worddict.get(check, None) != None:
      position.append(check)
  if len(position) == 0:
    return []
  return position

# all possible variations of cmudict for tokenized sentence
def possibles(words, worddict):
  # [ [ word, word(2) ], [ word ] ]
  variations = []
  for word in words:
    position = possibles_word(word, worddict)
    #if len(position) == 0 and (word.endswith("s") or word.endswith("d")):
    #  position = possibles_word(word[:-1], wordlist)
    if len(position) == 0:
      return []
    variations.append(position)
  out = []
  for row in product(*variations):
    out.append(row)
  return out

# two fails in a row are a swap- count the first one
def distance(stress, meter):
  fail = 0
  lastfail = False
  for i in range(len(stress)):
    if stress[i] != meter[i] and stress[i] != '?':
      if lastfail:
        lastfail = False
      else:
        fail = fail + 1
        lastfail = True
    else:
      lastfail = False
  return fail 

# allow "broken lines", with one missing syllable in input
def meter_loose(stresses):
  stress = ''
  for str in stresses:
    if len(str) == 1:
      stress = stress + "?"
    else:
      stress = stress + str
  #print(stress)
  poss = []
  fail = 0
  lastfail = False
  for (name, meter) in meters.items():
    if len(stress) + 1 < len(meter) or len(stress) > len(meter):
      continue
    if len(stress) == len(meter):
      fail = distance(stress, meter)
    elif len(stress) + 1 == meter:
      fail = distance('?' + stress, meter)
      if fail > 1:
        fail = distance(stress + '?', meter)
    if fail < 2:
      poss.append(name)
  return poss

def getstress(words, stresses):
  stressarray = []
  for word in words:
    word = word.lower()
    stress = stresses.get(word, None)
    if stress == None:
      stressarray = []
      break
    else:
      s = ""
      for st in stress:
        s = s + st
      stressarray.append(s)
  return stressarray

def meter(stresses):
  stress = ''
  for str in stresses:
    stress = stress + str
  for (name, meter) in meters.items():
    if stress == meter:
      return name
  return 'prose'

data = [
[ "short!", ['1', '10']],
[ "long!", ['11001000000']],
[ "swap", ['01', '10', '0', '1', '0101']],
[ "correct", ['0101010101']],
[ "one", ['0111010101']],
[ "two!", ['0111010001']],
[ "first missing", ['101010101']],
[ "last missing", ['010101010']]
]

#print("Strict meter:")
#for test in data:
#    print("{0} -> {1}".format(test[0], meter(test[1])))
#
#print("Broken meter:")
#for test in data:
#    print("{0} -> {1}".format(test[0], meter_loose(test[1])))
#
#print(possibles(['a', 'word'], {'a':0, 'word':0, 'word(2)':0}))

          

