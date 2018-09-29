import stringdist

# meter from cmudict: ['0', '10', '10']

d10 = "0101010101"

meters = {"iambic_pentameter" : d10}

def distance(stress, meter):
  fail = 0
  for i in range(len(stress)):
    if stress[i] != meter[i] and stress[i] != '?':
      fail = fail + 1
  return fail

# allow "broken lines", with one missing syllable in input
def meter_loose(stresses):
  stress = ''
  for str in stresses:
    if len(str) == 1:
      stress = stress + "?"
    else:
      stress = stress + str
  print(stress)
  poss = []
  fail = 0
  for (name, meter) in meters.items():
    if len(stress) == len(meter):
      fail = distance(stress, meter)
    elif len(stress) + 1 == meter:
      fail = distance('?' + stress, meter)
      if fail > 1:
        fail = distance(stress + '?', meter)
    print("{0}, {1}".format(name, fail))
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
['1', '10'],
['01', '10', '0', '1', '01', '0101'],
['0101010101'],
['0111010101'],
['0111010001'],
['101010101'],
['101010101'],
['010101010']
]

for test in data:
    print(meter(test))

for test in data:
    print(meter_loose(test))


          

