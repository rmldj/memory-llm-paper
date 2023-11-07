import numpy as np
import re

from pythia import pythia


# load results based on identifier

DIR = '../results'  

def load(identifier, version='original'):
    if not identifier.endswith('_' + version):
        identifier += '_' + version
    fname = DIR + '/' + identifier + '.npz'
    probs = np.load(fname)['probs']
    answers = np.load(fname)['answers']
    return probs, answers


# utilities for analyzing results

nouns = np.load('nouns.npz')['arr_0']
nouns = np.append(nouns, 48251)
nouns = np.append(nouns, 40959)

words = np.arange(50400)
exclude = np.array([220, 13, 764])
words = np.setdiff1d(words, exclude)


def rankprob_old(probabilities, token, token_subset=np.arange(50400)):
    ps = probabilities[token_subset]
    ind = np.argsort(ps)[::-1]
    sorted_tokens = token_subset[ind]
    sorted_ps = ps[ind]
    i0 = np.where(sorted_tokens==token)[0][0]
    p = sorted_ps[i0]/np.sum(sorted_ps)
    rank = i0 + 1
    return rank, p

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


def summarize(probs, answers, length, pythia_family=False, bare=False):

    subset = nouns
    if bare and not pythia_family:
        subset = words
    if pythia_family:
        subset = None

    n = len(answers)
    ranks = np.zeros(n, dtype=int)

    for i in range(n):
        if pythia_family:
            ans = pythia[answers[i]]
        else:
            ans = answers[i]
        r, p = rankprob(probs[i], ans, subset)
        ranks[i] = r

    corr = (ranks==1).astype(int)

    # reshape into N x num_queries
    corr2 = corr.reshape(-1, length)
    num_correct = np.sum(corr2, axis=1)
    means = np.mean(corr2, axis=1)

    acc_mean = np.mean(means)
    acc_std = np.std(means)

    num_correct_mean = np.mean(num_correct)
    num_correct_std = np.std(num_correct)

    accs = np.zeros(length)
    for i in range(length):
        accs[i] = np.mean(corr2[:,i])

    return acc_mean, acc_std, num_correct_mean, num_correct_std, accs


def get_length(identifier):
    matches = re.search(r'_l(\d+)_', identifier)
    return int(matches.group(1))

