
from sets import Set
from collections import Counter
import itertools

import cmudict
import arpabets


class Decoder:
  
  pho_list = ['IY', 'AW', 'DH', 'AY', 'HH', 'CH', 'JH', 'ZH', 'D', 'NG', 'TH', 'AA', 'B', 'AE', 'EH', 'G', 'F', 'AH', 'K', 'M', 'L', 'AO', 'N', 'IH', 'S', 'R', 'EY', 'T', 'W', 'V', 'Y', 'Z', 'ER', 'P', 'UW', 'SH', 'UH', 'OY', 'OW']
  
  # words for phoneme strings up to 10 long
  # dicts = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
  dicts = [{}] * 30

  # build reverse dict of phoneme->word, but only for words in our training set
  def __init__(self, reverse_dict, arpabets_mgr):
    self.reverse_dict = reverse_dict
    self.wordlist = Set([])
    for word in open("blobs/wordlist", "r"):
      word = word[0:-1]
      self.wordlist.add(word)
    #print("wordlist: {0}".format(list(self.wordlist)[0:5]))
    single_rev = {}
    for key in reverse_dict:
      word = reverse_dict[key]
      if word in self.wordlist:
        single_rev[key] = word
    self.single_dict = single_rev
    #print(short_rev)
    phomap = {}
    for pho in self.pho_list:
      phomap[pho] = Set([])
    #print("Phomap empty = " + str(phomap))
    for key in self.single_dict.keys():
      #print(key)
      good = True
      for pho in key.split(" "):
        if arpabets_mgr.get_encoding(pho) == 0:
          good = False
      if good:
        for pho in key.split(" "):
	  word = self.reverse_dict[key]
          if word.endswith(")"):
            word = word[0:-3]
          if word in self.wordlist:
            phomap[pho].add(word)
        #print(key + " len = " + str(len(key)))
        phodict = self.dicts[key.count(" ")]
    for key in reverse_dict.keys():
      #print(key)
      good = True
      for pho in key.split(" "):
        if arpabets_mgr.get_encoding(pho) == 0:
          good = False
      if good:
        phodict = self.dicts[key.count(" ")]
        phodict[key] = reverse_dict[key]
    self.pho2words = phomap

  def getwords(self, arpa_list, scores):
    #print(arpa_list)
    words = Counter()
    for i in range(len(arpa_list)):
      #print("{0} -> {1}".format(pho, self.pho2words[pho]))
      for word in self.pho2words[arpa_list[i]]:
        words[word] += scores[i]
    #print(words)
    #for key in words.most_common(100):
      #print(key)
    return words

  def decodewords(self, arpa_list):
    #print(arpa_list)
    first = 0
    last = 1
    words = Counter()
    while first < len(arpa_list):
      word = " ".join(arpa_list[first:last])
      #print(word)
      if word in self.reverse_dict:
        #print("{0} -> {1}".format(word, self.reverse_dict[word]))
        words[self.reverse_dict[word]] += 1
        first = last
        last = first + 1
      else:
        last = last + 1
    if first == len(arpa_list):
      return words
    else:
      return None

  def decode_sentence(self, arpa_list, limit):
    longest_word = 12

    def recurse(arpa_list, offset, limit):
      end = min(offset + longest_word, limit)
      print("checking {0}".format(arpa_list[offset:end+1]))
      for i in range(offset+1,end+1):
        sl = arpa_list[offset:i]
        key = " ".join(arpa_list[offset:i+1])
        if key in self.dicts[i - offset]:
          print(" y: " + key)
          first = self.dicts[i - offset][key]
          rest = []
          for l in recurse(arpa_list, i + len(sl), limit):
            rest.append(l)
          if len(rest) > 0:
            yield [first, rest]
          else:
            yield [first]
        else:
          print(" n: " + key)
          yield ['!']

    # ['the(2)', [['suh', [['!']]], ['sun', []], ['sun', []]]]
    # ['the(2)', [['suh', [['!'], ['!'], ['!']]], ['sun', [['it(2)', []]]], ['!'], ['!'], ['sunlit', []]]]
    def do_unwrap(lol, unwrapped):
      if lol[0] == '!':
        return
      
    
      
        
    for x in recurse(arpa_list, 0, limit):
      print("Found: " + str(x))
      poss_array = []
    

if __name__ == "__main__":
  def check1(phonemes):
    scores = [1] * len(phonemes)
    print(scores)
    wordlist = decoder.getwords('DH AH S AH N L IH T AA N IH NG HH IY V IH NG OW V ER HH EH D'.split(' '), scores)
    #print(len(wordlist))
  (x, y, reverse_dict) = cmudict.load_dictionary()
  decoder = Decoder(reverse_dict, arpabets.arpabets())
  #wordcounter = check1('DH AH S AH N L IH T AA N IH NG HH IY V IH NG OW V ER HH EH D'.split(' '))
  #print(wordcounter.most_common(50))
  decoder.decode_sentence('DH AH S AH N'.split(' '), 5)
  decoder.decode_sentence('DH AH S AH N L IH T'.split(' '), 7)
  #decoder.decode_sentence('DH AH S AH N L IH T AA N IH NG HH IY V IH NG OW V ER HH EH D'.split(' '), 20)
  
#'AE N D AO L OW L IH M P AH S R IH NG Z W IH DH L AW D AH L AA R M Z'
#'AE N HH AH M B AH L CH IH R F AH L HH AE P IY L AH V IH NG B AE N D'
#'P ER EY D IH NG IH N AH K AA M M AH JH EH S T IH K EH R'
#'DH AH K AA M ER S AH V DH AH W ER L D W IH DH T AA N IY L IH M'
#'DH AH W EY T AH V Y IH R Z AO R W ER L D L IY K EH R Z DH AE T P R EH S'
#'K AH N JH EH K CH ER AH V DH AH P L UW M AH JH AE N D DH AH F AO R M'
#'AE N D HH AE N D IH N HH AE N D DH AH L AE F IH NG B EH L AE D R EH S'
#'AH N T IH L DH AE T AW ER DH AH W AO R F EH R L AE S T AH D DH EH R'
#'AE N D R AE M B L IH NG B R AE M B AH L B EH R IY Z P AH L P AE N D S W IY T'
