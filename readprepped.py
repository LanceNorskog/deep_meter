# Read prepped data in format:  text tab [syllables ]

import numpy as np

# read classified poetry lines: text tab [['syll', 'la', 'ble'], ...]
# clip to only most common syllables with syllable manager
# ['words', ...], [[[0,0,1,0], ...]]
def get_data(filename, arpabet_mgr, num_symbols):
    stop_arpabet = 0
    num_arpabets = arpabet_mgr.get_size()      
    lines = open(filename, 'r').read().splitlines()
    num_lines = len(lines)
    num_lines = 50000
    text_lines = []
    text_arpabets = []
    for i in range(0, len(lines)):
      if i == num_lines:
        break
      parts = lines[i].split("\t")
      syllables = literal_eval(parts[1])
      #print(syllables)
      arpas = []
      for s in syllables:
        for p in s:
          for x in p.split(' '):
            arpas.append(x)
      #print(arpas)
      if len(arpas) < num_symbols:
        text_lines.append(str(parts[0]))
        text_arpabets.append(arpas)
    num_lines = len(text_lines)
    label_array = np.zeros((num_symbols, num_lines, num_arpabets), dtype=np.int8)
    for i in range(0, num_lines):
      for j in range(num_symbols):
        label_array[j][i][stop_arpabet] = 1
        # variable-length list of syllables
        if j < len(text_arpabets[i]):
          enc = arpabet_mgr.get_encoding(text_arpabets[i][j])
          if enc >= 0 and enc < num_arpabets:
            label_array[j][i][enc] = 1
            label_array[j][i][stop_arpabet] = 0

    return (text_lines, label_array)

