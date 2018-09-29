import collections

# load cmudict-syllables
# dict {word -> [syllable list]

# from NLTK, overkill
# need arpabets for words not in cmulist!

stopword_1 = ["i", "me", "my", "we", "our", "ours", "you", "you're", "you've", "you'll", "you'd", "your", "yours", "he", "him", "his", "she", "she's", "her", "hers", "it", "it's", "its", "they", "them", "their", "theirs", "what", "which", "who", "whom", "this", "that", "that'll", "these", "those", "am", "is", "are", "was", "were", "be", "been", "have", "has", "had", "do", "does", "did", "a", "an", "the", "and", "but", "if", "or", "as", "of", "at", "by", "for", "with", "through", "to", "from", "up", "down", "in", "out", "on", "off", "then", "once", "here", "there", "when", "where", "why", "how", "all", "both", "each", "few", "more", "most", "some", "such", "no", "nor", "not", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "don't", "should", "now", "d", "ll", "m", "o", "re", "aren't", "shan", "shan't", "wasn", "won", "won't", ","]

cmudict = "/Users/l0n008k/open/data/cmudict_0.6.syllablized.txt"
cmudict = "/home/lance/open/data/cmudict_0.6.syllablized.txt"

def load_syllables(do_stresses):
  syllables = {}
  stresses = {}
  if do_stresses:
    for stopword in stopword_1:
      stresses[stopword] = [ "1" ]
  x = 0
  with open(cmudict, "r") as ins:
    for line in ins:
      if line.startswith("#"):
        continue
      words = line.split(" ")
      key = words[0].lower()
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
        elif arpa.endswith("1"):
          stressarray.append("1")
          arpa = arpa[:-1]
        if arpa == "-" and len(syll) > 0:
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
      syllables[key] = syllarray
      if do_stresses:
        stresses[key] = stressarray
      x = x + 1
  return (syllables, stresses)

#(syllables, stresses) = load_syllables(True)
#print(stresses["and"])

#x = collections.Counter()
