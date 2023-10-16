import numpy as np
import sys
import re
import os

# same as errors.py but IGNORING nouns

if len(sys.argv)<3:
    print('usage: python errors.py FILE.npz POSITION')
    print('Lists possible errors for the fact at POSITION (starting from 1)')
    quit()

fname = sys.argv[1]
basename = os.path.basename(fname)
pos = int(sys.argv[2])

print(basename)
print('position', pos)
print()

probs = np.load(fname)['probs']
answers = np.load(fname)['answers']
n = len(answers)

# nouns = np.load('nouns.npz')['arr_0']
# nouns = np.append(nouns, 48251)
# nouns = np.append(nouns, 40959)

if 'pythia' in fname:
    from pythia import pythia
    words = None
    tokens = np.load('tokens_pythia.npz', allow_pickle=True)['arr_0']
else:
    pythia = None
    words = np.arange(50400)
    #exclude = np.array([220, 13, 764])
    #words = np.setdiff1d(words, exclude)
    tokens = np.load('tokens.npz', allow_pickle=True)['arr_0']

# memory_lives-in_l12_d1_direct_original.npz
# memory_complex_has-a_fillall_l7_original.npz
matches = re.search(r'_l(\d+)_', basename)
l = int(matches.group(1))

for i in range(n):
    if i%l==pos-1:
        ps = probs[i]
        if pythia is None:
            ans = answers[i]
        else:
            ans = pythia[answers[i]]
        if words is not None:
            ps = ps[words]
        ind = np.argsort(ps)[::-1]
        if words is not None:
            toks = words[ind]
        else:
            toks = ind
        #print(toks[0], ans)
        if toks[0]==ans:
            print('     ', i, tokens[ans], '|', end='')
        else:
            print('ERROR', i, tokens[ans], '|', end='')
        for j in range(10):
            print(tokens[toks[j]], end='')
            if toks[j]==ans:
                break
        print()


