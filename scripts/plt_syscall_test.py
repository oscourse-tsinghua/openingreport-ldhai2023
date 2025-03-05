import matplotlib.pyplot as plt
import numpy as np

plt.rc('font', family='Times New Roman')
plt.figure(figsize=(8, 5))
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
# 构造x轴刻度标签、数据
labels = ['8', '16', '32', '64', '128', '256', '512']
sync = [8172, 8172, 8172, 8172, 8172, 8172, 8172]
async_up = [22732, 12314, 7121, 6234, 6214, 6106, 6136]
async_smp = [20079, 9614, 5684, 5406, 5404, 5293, 5286]

server_up = [0.125, 0.0625, 0.03125, 0.02656, 0.02617, 0.02519, 0.02519]
server_smp = [0.14375, 0.08125, 0.075, 0.04922, 0.0402, 0.03379, 0.03203]

x = np.arange(len(labels))  # x轴刻度标签位置
width = 0.3  # 柱子的宽度
# 计算每个柱子在x轴上的位置，保证x轴刻度标签居中
plt.bar(x - 1 * width, sync, width, label='sync', color = "#000000", edgecolor='black')
plt.bar(x, async_up, width, label='async-up', color = "dimgray", edgecolor='black')
plt.bar(x + 1 * width, async_smp, width, label='async-smp', color = "darkgray", edgecolor='black')
plt.ylabel('The average CPU cycles used by a single system call')
plt.xlabel('concurrency')
# plt.title('单个系统调用的占用的平均CPU周期数和')
# x轴刻度标签位置不进行计算
plt.xticks(x, labels=labels)
plt.legend(loc="upper left")

ax2 = plt.twinx()
ax2.set_ylabel("Trapped frequency(trap count / syscall count)")
ax2.set_ylim([0, 0.15])
plt.plot(labels, server_up, marker='.', c='black', ms=5, linewidth='1', label="server-up")
plt.plot(labels, server_smp, marker='.', c='black', linestyle='--', ms=5, linewidth='1', label="server-smp")
plt.legend(loc="upper right")

# plt.show()
plt.savefig("syscall_test.svg")