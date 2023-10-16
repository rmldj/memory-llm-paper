import numpy as np
import matplotlib.pyplot as plt


from utils import load, summarize


plt.rcParams.update({'font.size':18})
plt.rcParams.update({'legend.fontsize':14})
plt.rcParams['figure.constrained_layout.use'] = True

seeds = [555, 666, 1621, 137, 0]

# data from experiments4tri

def collect_data(pattern):
    probsall = []
    ansall = []
    for seed in seeds:
        identifier = pattern.format(seed)
        probs, answers = load(identifier)
        probsall.append(probs)
        ansall.append(answers)
    probsall = np.vstack(probsall)
    ansall = np.hstack(ansall)
    acc_mean, acc_std, num_correct_mean, num_correct_std, accs = summarize(probsall, ansall, 10)
    return acc_mean, acc_std, accs

baseline_acc_mean, baseline_acc_std, baseline_accs = collect_data('memory_complex2_has-a_fillall_l10_seed{}')
independent_acc_mean, independent_acc_std, independent_accs = collect_data('memory_complex2_has-a_independent_l10_seed{}')
complementary_acc_mean, complementary_acc_std, complementary_accs = collect_data('memory_complex2_complementary_has-a_is-a_l10_seed{}')
same_acc_mean, same_acc_std, same_accs = collect_data('memory_complex2_has-a_is-a_l10_seed{}')

print('baseline      {:.3f}+-{:.3f}'.format(baseline_acc_mean, baseline_acc_std))
print('independent   {:.3f}+-{:.3f}'.format(independent_acc_mean, independent_acc_std))
print('complementary {:.3f}+-{:.3f}'.format(complementary_acc_mean, complementary_acc_std))
print('same          {:.3f}+-{:.3f}'.format(same_acc_mean, same_acc_std))

ls = np.arange(1, 11)

plt.figure()
plt.plot(ls, baseline_accs, 'o-', alpha=0.5, label='baseline')
plt.plot(ls, independent_accs, 'o-', alpha=0.5, label='countries and colours')
plt.plot(ls, complementary_accs, 'o-', alpha=0.5, label='different persons')
plt.plot(ls, same_accs, 'o-', alpha=0.5, label='same persons')
plt.xlabel('position')
plt.ylabel('mean accuracy')
plt.ylim(0, 1)

ax =plt.gca()
ax.set_xticks(ls, minor=False)

plt.legend()

plt.savefig('fig_interference2.png')

