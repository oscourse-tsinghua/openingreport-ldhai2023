import matplotlib.pyplot as plt
import numpy as np

plt.rc('font', family='Times New Roman')
plt.figure(figsize=(8, 5))
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
# 构造x轴刻度标签、数据
labels = ["1", "2", "4", '8', '16', '32']
sync = [9806, 9806, 9806, 9806, 9806, 9806]
async_up = [21278, 14776, 8545, 7480, 7456, 7433]
async_smp = [19094, 11536, 6820, 6487, 6484, 6490]
taic_up = [12216, 9927, 8588, 7242, 7201, 7168]
taic_smp = [7517, 6562, 6097, 5857, 5774, 5759, ]
# taic_up = [8588, 7442, 7501, 7368, 7469]
# taic_smp = [6097, 5857, 5774, 5759, 5858, ]

# taic_up = [12216, 9927, 8588, 7442, 7501, 7368, 7469]
# taic_smp = [11517, 8562, 6097, 5857, 5774, 5759, 5858, ]

server_up = [1, 0.5, 0.249,0.1254, 0.0625, 0.03125]
server_smp = [1, 0.5, 0.247, 0.1517, 0.1462, 0.075]

x = np.arange(len(labels))  # x轴刻度标签位置
width = 0.15  # 柱子的宽度
# 计算每个柱子在x轴上的位置，保证x轴刻度标签居中
plt.bar(x - 2 * width, sync, width, label='sync', color = "black", edgecolor='black')
plt.bar(x - 1 * width, async_up, width, label='async-up', color = "brown", edgecolor='black')
plt.bar(x, async_smp, width, label='async-smp', color = "dodgerblue", edgecolor='black')
plt.bar(x + 1 * width, taic_up, width, label='taic-up', color="cyan", edgecolor='black')
plt.bar(x + 2 * width, taic_smp, width, label='taic-smp', color="m", edgecolor='black')
plt.ylabel('The average CPU cycles used by a single system call')
plt.xlabel('concurrency')
# plt.title('单个系统调用的占用的平均CPU周期数和')
# x轴刻度标签位置不进行计算
plt.xticks(x, labels=labels)
plt.legend(loc="upper left")

ax2 = plt.twinx()
ax2.set_ylabel("Trapped frequency(trap count / syscall count)")
ax2.set_ylim([0, 1])
plt.plot(labels, server_up, marker='.', c='black', ms=5, linewidth='1', label="server-up")
plt.plot(labels, server_smp, marker='.', c='black', linestyle='--', ms=5, linewidth='1', label="server-smp")
plt.legend(loc="upper right")

# plt.show()
plt.savefig("syscall_test.pdf")