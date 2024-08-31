#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib.patheffects as path_effects
from os import system


data = pd.read_csv('latency_data.txt', sep=" ", header=None)

def calc_stats(data):
    max_us = np.max(data)[0]
    mean_us = np.mean(data)[0]
    min_us = np.min(data)[0]
    print('Samples: %d' % (data[0].count()))
    print('Max time: %d' % (max_us))
    print('Min time: %d' % (min_us))
    print('Median time: %d' % (mean_us))
    return [max_us, mean_us, min_us]


def get_median_label(ax, fmt='.1f'):
    lines = ax.get_lines()
    boxes = [c for c in ax.get_children() if type(c).__name__ == 'PathPatch']
    lines_per_box = int(len(lines) / len(boxes))
    for median in lines[4:len(lines):lines_per_box]:
        x, y = (data.mean() for data in median.get_data())
        # choose value depending on horizontal or vertical plot orientation
        value = x if (median.get_xdata()[1] - median.get_xdata()[0]) == 0 else y
        # text = ax.text(x, y, f'{value:{fmt}}', ha='center', va='center',
        #                fontweight='bold', color='white')
        # # create median-colored border around white text for contrast
        # text.set_path_effects([
        #     path_effects.Stroke(linewidth=3, foreground=median.get_color()),
        #     path_effects.Normal(),
        # ])

        return value


[max_us1, mean_us1, min_us1] = calc_stats(data)
x_min = min_us1

# Configure font defaults
# plt.rcParams.update({'font.size': 10, 'font.weight': 'bold'})
plt.rcParams.update({'font.size': 10})
plt.rc('pdf', fonttype=42)  # embed pdf fonts (truetype)

# Create axis
f, (ax_box, axs) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .85)})

# Create Plots
boxplot = sns.boxplot(data=data[0], orient="h", ax=ax_box, linewidth=1.2, color='cornflowerblue', saturation=1.0)
sns.histplot(data=data[0], bins=8000, element="step", 
    stat="frequency",
    label='Max: %d us\nMin: %d us\nMedian: %d us' % (max_us1, min_us1, get_median_label(boxplot)),
    color='cornflowerblue')

for i,box in enumerate(boxplot.artists):
    box.set_edgecolor('black')
    # iterate over whiskers and median lines
    for j in range(6*i,6*(i+1)):
         boxplot.lines[j].set_color('black')

# Graph Limits
axs.set_xlim(left=20, right=150)
ax_box.set_ylim(-0.7,0.7)

# Texts
axs.legend(labelspacing=0.8, prop={'style': 'italic'})
plt.xlabel('') 
# plt.xlabel('BLEDefender Bridging Latency (us)') 
plt.ylabel('Frequency')
plt.yticks([])
boxplot.set(yticklabels=[])
axs.grid(alpha=0.6)

# Size Adjust
plt.subplots_adjust(top=0.5, right=0.9, left=0.1, hspace=0.08)

# Save/Show figure
plt.savefig('interception_latency.pdf')  # requires latest lxml
system("pdfcrop interception_latency.pdf --margin 0.1 interception_latency.pdf")


plt.show()