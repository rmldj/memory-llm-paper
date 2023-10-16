import numpy as np
import matplotlib.pyplot as plt

from utils import load, summarize


plt.rcParams.update({'font.size':18})
plt.rcParams.update({'legend.fontsize':14})
plt.rcParams['figure.constrained_layout.use'] = True


# supplementary data from experiments1bis

seeds = [555, 666, 1621, 137, 0]




def collect_data(variant, L):
    accs = []
    stds = []
    accs_pos = []
    for seed in seeds:
        identifier = 'memory_{}_l{}_d1_direct_seed{}'.format(variant, L, seed)
        probs, answers = load(identifier)
        acc_mean, acc_std, _, _, acc_pos = summarize(probs, answers, L)
        accs.append(acc_mean)
        stds.append(acc_std)
        accs_pos.append(acc_pos)
    return np.array(accs), np.array(stds), np.array(accs_pos)

accs_livesin, stds_livesin, pos_livesin20 = collect_data('lives-in', 20)
accs_hasa, stds_hasa, pos_hasa20 = collect_data('has-a', 20)
accs_isa, stds_isa, pos_isa20 = collect_data('is-a', 20)

pos_livesin20 = np.mean(pos_livesin20, axis=0)
pos_hasa20 = np.mean(pos_hasa20, axis=0)
pos_isa20 = np.mean(pos_isa20, axis=0)


ns = np.arange(1, 21)

plt.figure()
plt.plot(ns, pos_livesin20, 'o-', alpha=0.5, label='lives-in')
plt.plot(ns, pos_hasa20, 'o-', alpha=0.5, label='has-a')
plt.plot(ns, pos_isa20, 'o-', alpha=0.5, label='is-a')

plt.ylim(0, 1)
plt.ylabel('mean accuracy')

plt.xticks([1, 5, 10, 15, 20])
ax =plt.gca()
ax.set_xticks(ns, minor=True)
plt.xlabel('position')
plt.legend()

plt.legend()

plt.savefig('fig_overall2bis.png')


Ls = [6, 12, 16, 20]
pos_hasa = dict()
for L in Ls:
    _, _, pos = collect_data('has-a', L)
    pos_hasa[L] = np.mean(pos, axis=0)



plt.figure()
for L in Ls:
    plt.plot(range(1, L+1), pos_hasa[L], 'o-', alpha=0.5, label='has-a {} facts'.format(L))

plt.ylim(0, 1)
plt.ylabel('mean accuracy')

plt.xticks([1, 5, 10, 15, 20])
ax =plt.gca()
ax.set_xticks(ns, minor=True)
plt.xlabel('position')
plt.legend()

plt.legend()

plt.savefig('fig_overall3bis.png')
