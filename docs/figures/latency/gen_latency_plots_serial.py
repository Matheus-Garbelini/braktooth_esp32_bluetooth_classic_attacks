#!/usr/bin/env python3

# %%

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data1 = pd.read_csv('latency_5.10_4.txt', sep=" ", header=None)
data2 = pd.read_csv('latency_5.10_4_rt.txt', sep=" ", header=None)

max_us1 = np.max(data1)[0]
mean_us1 = np.mean(data1)[0]
min_us1 = np.min(data1)[0]
max_us2 = np.max(data2)[0]
mean_us2 = np.mean(data2)[0]
min_us2 = np.min(data2)[0]

print('Samples: %d' % (data1[0].count()))
print('Max time: %d' % (max_us1))
print('Min time: %d' % (min_us1))
print('Median time: %d' % (mean_us1))


# Configure font defaults
plt.rcParams.update({'font.size': 11, 'font.weight': 'bold'})
plt.rc('pdf', fonttype=42)  # embed pdf fonts (truetype)

# Configure Grid
plt.grid(alpha=0.6)

# Main Plot code
plt.hist(data1, bins=100, range=[100, 500], density=True,
         histtype='step', linewidth=1.8, linestyle='-',
         label='Kernel 5.10\nMax: %d us\nMin: %d\nMean: %d' % (max_us1, min_us1, mean_us1))

plt.axvline(mean_us1, color='k', linestyle='-',
            linewidth=1.3, alpha=0.8, label='_nolegend_')


plt.hist(data2, bins=100, range=[100, 500], histtype='step',
         linewidth=1.8, linestyle='--', density=True,
         label='Kernel 5.10 RT\nMax: %d us\nMin: %d\nMean: %d' % (max_us2, min_us2, mean_us2))

plt.axvline(min_us1, color='k', linestyle='-',
            linewidth=1.3, alpha=0.8, label='_nolegend_')

min_ylim, max_ylim = plt.ylim()
plt.text(180, max_ylim*1.01, '%d us' % (min_us1))
plt.text(270, max_ylim*1.01, '%d us' % (mean_us1))


# Configure Legend
# plt.legend(labelspacing=0.1)
plt.legend(labelspacing=1.0, prop={'weight': 'bold', 'style': 'italic'})



# plt.xlabel('Interception Round Trip Time (us)')
# plt.xlabel('Interceptssion Round Trip Time (us)', fontweight='bold')

# Hide yaxis label
plt.gca().axes.yaxis.set_visible(False)
plt.subplots_adjust(top=0.5, right=0.95, left=0.05)
plt.gca().set_xlim(left = 150, right=500)
plt.gca().set_ylim(top=0.0125)

# Save/Show figure
# plt.savefig('interception_latency.svg')
plt.savefig('interception_latency.pdf')  # requires latest lxml
plt.show()

# %%
