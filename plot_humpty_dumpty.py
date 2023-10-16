import numpy as np
import matplotlib.pyplot as plt
import sys

from utils import load, summarize


plt.rcParams.update({'font.size':18})
plt.rcParams.update({'legend.fontsize':14})
plt.rcParams['figure.constrained_layout.use'] = True



# data from experiments3tri

ns = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]

accs = np.zeros(len(ns))
stds = np.zeros(len(ns))

for i, n in enumerate(ns):
    identifier = 'memory_has-a_l10_d{}_direct'.format(100 + n)
    probs, answers = load(identifier, version='original')
    acc_mean, acc_std, _, _, _ = summarize(probs, answers, 10)
    accs[i] = acc_mean
    stds[i] = acc_std

ls = [25, 35]

plt.figure()

plt.plot(ns, accs, 'o-', alpha=0.5, color='tab:brown', label='Humpty Dumpty')

lw = 3
plt.plot(ls, [0.745]*2, '-', alpha=0.5, color='tab:blue', label='baseline', linewidth=lw)
plt.plot([32, 42], [0.686]*2, '-', alpha=0.5, color='tab:orange', label='countries and colours', linewidth=lw)
plt.plot(ls, [0.633]*2, '-', alpha=0.5, color='tab:green', label='different persons', linewidth=lw)
plt.plot(ls, [0.324]*2, '-', alpha=0.5, color='tab:red', label='same persons', linewidth=lw)

#plt.errorbar(ns, accs, yerr=stds, fmt='o', capsize=3, ecolor='0.9', alpha=0.5, color='tab:brown')
plt.ylim(0, 1)
plt.xlim(0, 160)
plt.xlabel('repetitions of "Humpty Dumpty. "')
plt.ylabel('mean accuracy')
plt.legend(loc='lower right')

plt.savefig('fig_humptydumpty_updated.png')

plt.figure()

plt.plot(ns, accs, 'o-', alpha=0.5, color='tab:brown', label='Humpty Dumpty')


#plt.errorbar(ns, accs, yerr=stds, fmt='o', capsize=3, ecolor='0.9', alpha=0.5, color='tab:brown')
plt.ylim(0, 1)
plt.xlim(0, 160)
plt.xlabel('repetitions of "Humpty Dumpty. "')
plt.ylabel('mean accuracy')
plt.legend(loc='lower right')

plt.savefig('fig_humptydumpty_updated_bare.png')


# OUTDATED!!
# NOW USE 10*humpty dumpty before and after
# this gives effective lengths = 10+10+10=30 for baseline, complementary, same
# and 10+101/6+10 = 37 for independent 

# >>> from transformers import AutoTokenizer
# >>> from memory import *
# >>> tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")
# >>> tokenizer('Humpty Dumpty. ').input_ids
# [32661, 5835, 30933, 5835, 13, 220]
# >>> len(tokenizer('Humpty Dumpty. ').input_ids)
# 6
# >>> len(tokenizer(distractor[1]).input_ids)
# 32
# >>> len(tokenizer(distractor[6]).input_ids)
# 24
# >>> len(tokenizer(distractor[99]).input_ids)
# 101
# >>> len(tokenizer('Paul has a guitar. ').input_ids)
# 6
# >>> 101/6
# 16.833333333333332
# >>> (32+24)/6
# 9.333333333333334
# >>> (32+24+101)/6
# 26.166666666666668
# >>> 



# (py37) romuald@rtx:/storage_0/romuald/PRACA/MEMORY/memory$ time python plot_interference2.py 
# baseline      0.745+-0.128
# independent   0.686+-0.139
# complementary 0.633+-0.139
# same          0.324+-0.126
