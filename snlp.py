# read S-tree format from nltk.parse.stanford.GenericStanfordParser.parse_sents() method
# really just MultiNLI data
# generate certain sentence or clause variations

from nltk.tree import Tree

# TODO: walk tree and yield acceptable variations. For instance, remove adjectives and adverbs.

# break sentence
def parse(sentence):
    return Tree.fromstring(sentence)

def clauses(t, _min=0, _max=1000):
    out = {}
    for t2 in t.subtrees():
        t2 = flatten(t2)
        if len(t2) >= _min and len(t2) <= _max:
            out[' '.join(t2)] = 0
    return out.keys()

def flatten(t):
    out = []
    for x in t.flatten():
        out.append(x)
    return out


# sample = '(ROOT (S (NP (DT This) (NN site)) (VP (VBZ includes) (NP (NP (NP (DT a) (NN list)) (PP (IN of) (NP (DT all) (NN award) (NNS winners)))) (CC and) (NP (NP (DT a) (JJ searchable) (NN database)) (PP (IN of) (NP (NNP Government) (NNP Executive) (NNS articles)))))) (. .)))'
sample = '(ROOT (S (NP (PRP I)) (VP (VP (VBP like) (NP (PRP him)) (PP (IN for) (NP (DT the) (JJS most) (NN part)))) (, ,) (CC but) (VP (MD would) (ADVP (RB still)) (VP (VB enjoy) (S (VP (VBG seeing) (S (NP (NN someone)) (VP (VB beat) (NP (PRP him))))))))) (. .)))'

if __name__ == '__main__':
    t = Tree.fromstring(sample)
    for x in clauses(t, _min=3, _max=10):
        print(x)
