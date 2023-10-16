import numpy as np
import matplotlib.pyplot as plt

from utils import load, summarize

plt.rcParams.update({'font.size':18})
plt.rcParams.update({'legend.fontsize':14})
plt.rcParams['figure.constrained_layout.use'] = True


data = [0.5555555555555557,
    0.38962962962962966,
    0.38814814814814824,
    0.1777777777777777,
    0.2637037037037038,
    0.2266666666666668,
    0.1837037037037038,
    0.21777777777777785,
    0.1451851851851853,
    0.22962962962962974,
    0.19407407407407418,
    0.19111111111111123,
    0.1377777777777779,
    0.23851851851851857,
    0.2577777777777779,
    0.24888888888888894,
    0.3866666666666667,
    0.4103703703703705,
    0.5570370370370371,
    0.8074074074074076]

Ls = np.arange(1, 21)



# supplementary data from experiments1bis

seeds = [555, 666, 1621, 137, 0]




def collect_data(variant, L, network='original', pythia_family=False):
    accs = []
    stds = []
    accs_pos = []
    for seed in seeds:
        identifier = 'memory_{}_l{}_d1_direct_seed{}'.format(variant, L, seed)
        probs, answers = load(identifier, network)
        acc_mean, acc_std, _, _, acc_pos = summarize(probs, answers, L, pythia_family=pythia_family)
        accs.append(acc_mean)
        stds.append(acc_std)
        accs_pos.append(acc_pos)
    return np.array(accs), np.array(stds), np.array(accs_pos)

accs_hasa, stds_hasa, pos_hasa20 = collect_data('has-a', 20)
pos_hasa20 = np.mean(pos_hasa20, axis=0)

_, _, pos_pythia = collect_data('has-a', 20, network='pythia-6.9B', pythia_family=True)
pos_pythia = np.mean(pos_pythia, axis=0)


plt.figure()

plt.plot(Ls, data, 'o-', alpha=0.5, color='k', label='human data')
plt.plot(Ls, pos_hasa20, 'o-', alpha=0.5, color='tab:orange', label='GPT-J')


plt.ylim(0, 1.05)
plt.ylabel('mean accuracy')

plt.xticks([1, 5, 10, 15, 20])
ax = plt.gca()
ax.set_xticks(Ls, minor=True)

plt.xlabel('position')

plt.legend(loc='upper center')

plt.savefig('fig_glanzer_cunitz_gptj.png')


plt.figure()

plt.plot(Ls, data, 'o-', alpha=0.5, color='k', label='human data')
plt.plot(Ls, pos_hasa20, 'o-', alpha=0.5, color='tab:orange', label='GPT-J')
plt.plot(Ls, pos_pythia, 'o-', alpha=0.5, color='tab:red', label='pythia 6.9B')


plt.ylim(0, 1.05)
plt.ylabel('mean accuracy')

plt.xticks([1, 5, 10, 15, 20])
ax = plt.gca()
ax.set_xticks(Ls, minor=True)

plt.xlabel('position')

plt.legend(loc='upper center')

plt.savefig('fig_glanzer_cunitz.png')

plt.figure()

plt.plot(Ls, data, 'o-', alpha=0.5, color='k', label='human data')


plt.ylim(0, 1.05)
plt.ylabel('mean accuracy')

plt.xticks([1, 5, 10, 15, 20])
ax = plt.gca()
ax.set_xticks(Ls, minor=True)

plt.xlabel('position')

plt.legend(loc='upper center')

plt.savefig('fig_glanzer_cunitz_bare.png')

