import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

plt.rc('font',family='Times New Roman')
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'


labels = ['Interrupt', 'Polling', 'Hybrid polling']
lantency = [10559, 6968, 8172]
CPU_utilization = [0.97, 0.57, 0.92]
width = 0.3  # 柱子的宽度

fig, ax1 = plt.subplots(figsize=(5, 5))
x = np.arange(len(labels))  # x轴刻度标签位置
plt.xticks(x, labels=labels)
ax1.bar(x - width / 2, lantency, width, label='lantency', color = "black", edgecolor='black')
ax1.set_ylabel("lantency(cpu cycles)")

ax2 = ax1.twinx()
ax2.set_ylabel("CPU Utilization")
ax2.set_ylim([0.5, 1])
plt.bar(x + width / 2, CPU_utilization, width, label='CPU utilization', color = "grey", edgecolor='black')

fig.legend(loc='upper left', bbox_to_anchor=(0.1, 1), bbox_transform=ax1.transAxes)

plt.savefig("epoll_test.svg")