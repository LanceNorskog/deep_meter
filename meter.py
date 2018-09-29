import stringdist

# meter from cmudict: ['0', '10', '10']

d10 = "0101010101"

meters = {"iambic_pentameter" : d10}

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

#print("Broken meter:")
#for test in data:
#    print("{0} -> {1}".format(test[0], meter_loose(test[1])))


          

