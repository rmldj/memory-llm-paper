import numpy as np
import matplotlib.pyplot as plt

from utils import load, summarize


plt.rcParams.update({'font.size':18})
plt.rcParams.update({'legend.fontsize':14})
plt.rcParams['figure.constrained_layout.use'] = True


# data from RUN_PYTHIA
seeds = [555, 666, 1621, 137, 0]




def collect_data(variant, L, network, pythia_family=True):
    accs = []
    stds = []
    accs_pos = []
    for seed in seeds:
        identifier = 'memory_{}_l{}_d1_direct_seed{}'.format(variant, L, seed)
        probs, answers = load(identifier, version=network)
        acc_mean, acc_std, _, _, acc_pos = summarize(probs, answers, L, pythia_family=pythia_family)
        accs.append(acc_mean)
        stds.append(acc_std)
        accs_pos.append(acc_pos)
    return np.array(accs), np.array(stds), np.array(accs_pos)

pythia_variants = ['70m', '410m', '1.4B', '2.8B', '6.9B']

pos = dict()
accs = dict()

for pythia_variant in pythia_variants:
    accsall, _, pos20 = collect_data('has-a', 20, 'pythiav0-{}'.format(pythia_variant))
    pos[pythia_variant] = np.mean(pos20, axis=0)
    accs[pythia_variant] = np.mean(accsall)


accsall, _, pos20 = collect_data('has-a', 20, 'original', pythia_family=False)
pos['GPT-J'] = np.mean(pos20, axis=0)
accs['GPT-J'] = np.mean(accsall)


networks = ['70m', '410m', '1.4B', '2.8B', '6.9B', 'GPT-J']

ns = np.arange(1, 21)

plt.figure()
for network in networks:
    plt.plot(ns, pos[network], 'o-', alpha=0.5, label=network)


plt.ylim(0, 1)
plt.ylabel('mean accuracy')

plt.xticks([1, 5, 10, 15, 20])
ax =plt.gca()
ax.set_xticks(ns, minor=True)
plt.xlim(0, 27.5)
plt.xlabel('position')
plt.legend()



plt.savefig('fig_pythiav02sel.png')



