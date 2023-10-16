import numpy as np
import matplotlib.pyplot as plt

from utils import load, summarize


plt.rcParams.update({'font.size':18})
plt.rcParams.update({'legend.fontsize':14})
plt.rcParams['figure.constrained_layout.use'] = True

seeds = [555, 666, 1621, 137, 0]
nseeds = len(seeds)

L = 19

baseline = np.zeros((nseeds, L))
elaborations = np.zeros((nseeds, L))

for i, seed in enumerate(seeds):
    probs, answers = load('memory_has-a_l19_d1_direct_seed{}'.format(seed))
    acc_mean, acc_std, num_correct_mean, num_correct_std, accs = summarize(probs, answers, 19)
    baseline[i, :] = accs

    probs, answers = load('memory_has-a_l19_d1_direct_seed{}_elaborate5-10-15'.format(seed))
    acc_mean, acc_std, num_correct_mean, num_correct_std, accs = summarize(probs, answers, 19)
    elaborations[i, :] = accs



ls = np.arange(1, L+1)

plt.figure()
plt.plot(ls, np.mean(baseline, axis=0), 'o-', alpha=0.5, label='baseline')
plt.plot(ls, np.mean(elaborations, axis=0), 'o-', alpha=0.5, label='elaborations @5,10,15')
plt.xlabel('position')
plt.ylabel('mean accuracy')
plt.ylim(0, 1)

ax =plt.gca()
ax.set_xticks(ls, minor=True)

elabmean = np.mean(elaborations, axis=0)

dy1 = 0.15
dy2 = -0.1
plt.arrow(5, elabmean[4]+dy1, 0, dy2,  color='r',  head_length=.05, head_width=.2,
         length_includes_head=True)
plt.arrow(10, elabmean[9]+dy1, 0, dy2, color='r',  head_length=.05, head_width=.2,
         length_includes_head=True)
plt.arrow(15, elabmean[14]+dy1, 0, dy2, color='r',  head_length=.05, head_width=.2,
         length_includes_head=True)

plt.legend(loc='upper center')



plt.savefig('fig_elaborations.png')



plt.figure()
plt.plot(ls, np.mean(baseline, axis=0), 'o-', alpha=0.5, label='baseline')
#plt.plot(ls, np.mean(elaborations, axis=0), 'o-', alpha=0.5, label='elaborations @5,10,15')
plt.xlabel('position')
plt.ylabel('mean accuracy')
plt.ylim(0, 1)

ax =plt.gca()
ax.set_xticks(ls, minor=True)

# elabmean = np.mean(elaborations, axis=0)

# dy1 = 0.15
# dy2 = -0.1
# plt.arrow(5, elabmean[4]+dy1, 0, dy2,  color='r',  head_length=.05, head_width=.2,
#          length_includes_head=True)
# plt.arrow(10, elabmean[9]+dy1, 0, dy2, color='r',  head_length=.05, head_width=.2,
#          length_includes_head=True)
# plt.arrow(15, elabmean[14]+dy1, 0, dy2, color='r',  head_length=.05, head_width=.2,
#          length_includes_head=True)

plt.legend(loc='upper center')



plt.savefig('fig_elaborations_bare.png')


