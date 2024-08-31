#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# %%

data1 = pd.read_csv('wifi_interception_5.11_lowlatency.txt', sep=" ", header=None)

max_us1 = np.max(data1)[0]
mean_us1 = np.mean(data1)[0]
min_us1 = np.min(data1)[0]


print('Samples: %d' % (data1[0].count()))
print('Max time: %d' % (max_us1))
print('Min time: %d' % (min_us1))
print('Median time: %d' % (mean_us1))

plt.grid(alpha=0.6)
plt.hist(data1, bins=100, range=[10, 200], density=True,
         histtype='step', linewidth=2, linestyle='-',
         label='Kernel 5.11\nMax: %d us\nMin: %d\nMean: %d' % (max_us1, min_us1, mean_us1))

plt.axvline(mean_us1, color='k', linestyle='-',
            linewidth=1, alpha=0.7, label='_nolegend_')


plt.axvline(min_us1, color='k', linestyle='-',
            linewidth=1, alpha=0.7, label='_nolegend_')

min_ylim, max_ylim = plt.ylim()
plt.text(22, max_ylim*1.01, '%d us' % (min_us1))
plt.text(87, max_ylim*1.01, '%d us' % (mean_us1))

# plt.subplots_adjust(top=0.5)
plt.legend(labelspacing=1.5)

plt.savefig('interception_latency_wifi.svg')
