import numpy as np
import re
import os
import sys

# same as summarize.py but IGNORING nouns

if len(sys.argv)<2:
    print('usage: python summarize.py FILE.npz')
    quit()

fname = sys.argv[1]
basename = os.path.basename(fname)

print(basename)
print()

probs = np.load(fname)['probs']
answers = np.load(fname)['answers']

# nouns = np.load('nouns.npz')['arr_0']
# nouns = np.append(nouns, 48251)
# nouns = np.append(nouns, 40959)


if 'pythia' in fname:
    from pythia import pythia
    words = None
else:
    pythia = None
    words = np.arange(50400)
    exclude = np.array([220, 13, 764])
    words = np.setdiff1d(words, exclude)

def rankprob(probabilities, token, token_subset=None):
    if token_subset is None:
        ps = probabilities
    else:
        ps = probabilities[token_subset]
    ind = np.argsort(ps)[::-1]
    if token_subset is None:
        sorted_tokens = ind
    else:
        sorted_tokens = token_subset[ind]
    sorted_ps = ps[ind]
    i0 = np.where(sorted_tokens==token)[0][0]
    p = sorted_ps[i0]/np.sum(sorted_ps)
    rank = i0 + 1
    return rank, p

n = len(answers)
ranks = np.zeros(n, dtype=int)

for i in range(n):
    if pythia is None:
        ans = answers[i]
    else:
        ans = pythia[answers[i]]
    r, p = rankprob(probs[i], ans, words)
    ranks[i] = r

corr = (ranks==1).astype(int)

# memory_lives-in_l12_d1_direct_original.npz
# memory_complex_has-a_fillall_l7_original.npz
matches = re.search(r'_l(\d+)_', basename)
l = int(matches.group(1))


# reshape into N x num_queries
corr2 = corr.reshape(-1, l)
num_correct = np.sum(corr2, axis=1)
means = np.mean(corr2, axis=1)

print('mean accuracy {:.3f}+-{:.3f}'.format(np.mean(means), np.std(means)))
print('number of correct words {:.2f}+-{:.2f}'.format(np.mean(num_correct), np.std(num_correct)))
print()

for i in range(l):
    print('accuracy at position {}: {:.3f}'.format(i+1, np.mean(corr2[:,i])))
    






