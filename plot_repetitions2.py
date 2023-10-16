import numpy as np
import matplotlib.pyplot as plt

from utils import load, summarize


plt.rcParams.update({'font.size':18})
plt.rcParams.update({'legend.fontsize':14})
plt.rcParams['figure.constrained_layout.use'] = True


# data from experiments6bis

Ls = [7, 9, 11, 13, 15, 17, 19]

def collect_data(pattern):
    accs = []
    stds = []
    for L in Ls:
        identifier = pattern.format(L)
        probs, answers = load(identifier)
        acc_mean, acc_std, _, _, _ = summarize(probs, answers, L)
        accs.append(acc_mean)
        stds.append(acc_std)
    return np.array(accs), np.array(stds)
    

accs_baseline, stds_baseline = collect_data('memory_complex2_has-a_fillall_l{}')
accs_repeated, stds_repeated = collect_data('memory_complex2_has-a_repeated_l{}')
accs_permuted, stds_permuted = collect_data('memory_complex2_has-a_permuted_l{}')
accs_adjacent_repeated, stds_adjacent_repeated = collect_data('memory_complex2_adjacent_has-a_repeated_l{}')
accs_adjacent_permuted, stds_adjacent_permuted = collect_data('memory_complex2_adjacent_has-a_permuted_l{}')


plt.figure()
plt.plot(Ls, accs_baseline, 'o-', alpha=0.5, label='baseline')
plt.plot(Ls, accs_adjacent_repeated, 'o-', alpha=0.5, label='repeated')
plt.plot(Ls, accs_adjacent_permuted, 'o-', alpha=0.5, label='repeated permuted')
plt.plot(Ls, accs_repeated, 'o-', alpha=0.5, label='repeated (separated)')
plt.plot(Ls, accs_permuted, 'o-', alpha=0.5, label='repeated permuted (separated)')

plt.ylim(0, 1)
plt.ylabel('mean accuracy')

plt.xticks(Ls)
plt.xlabel('length')

plt.legend()

plt.savefig('fig_repetitions2.png')



