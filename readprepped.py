# Read prepped data in format:  text tab [syllables ]

import numpy as np
from ast import literal_eval
import arpabets

# read classified poetry lines: text tab [['syll', 'la', 'ble'], ...]
# clip to only most common syllables with syllable manager
# ['words', ...], [[[0,0,1,0], ...]]
def get_data(filename, arpabet_mgr, num_symbols, max_lines=10000000000):
    stop_arpabet = 0
    num_arpabets = arpabet_mgr.get_size()      
    lines = open(filename, 'r').read().splitlines()
    text_lines = []
    text_arpabets = []
    if len(lines) > max_lines:
        lines = lines[:max_lines]
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

# read classified poetry lines: text tab [['syll', 'la', 'ble'], ...]
# clip to only most common syllables with syllable manager
# ['words', ...], [[[0,0,1,0], ...]]
def read_prepped(filename, syll_mgr, num_symbols, max_lines=1000000):
    num_syllables = syll_mgr.get_size()      
    lines = open(filename, 'r').read().splitlines()
    num_lines = min(max_lines, len(lines))
    text_lines = []
    text_sylls = []
    for i in range(0, len(lines)):
      if i == num_lines:
        break
      parts = lines[i].split("\t")
      label = utils.flatten(literal_eval(parts[1]))
      if len(label) == num_symbols:
        text_lines.append(str(parts[0]))
        text_sylls.append(label)
    num_lines = len(text_lines)
    label_array = np.zeros((num_symbols, num_lines, num_syllables), dtype=np.int8)
    for i in range(0, num_lines):
      for j in range(num_symbols):
        label_array[j][i][syll_mgr.get_encoding(text_sylls[i][j])] = 1
    return (text_lines, label_array)


if __name__ == "__main__":
    arpabet_mgr = arpabets.arpabets()
    data = get_data('prepped_data/gutenberg.iambic_pentameter', arpabet_mgr, 10)
    print("Read {} lines of text".format(len(data)))
