import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

plt.rc('font',family='Times New Roman')
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.figure(figsize=(8, 5))
# 构造x轴刻度标签、数据
labels = ['1', '2', '4', '8', '16', '32']
sync_up_fp = [3027, 3027, 3027, 3027, 3027, 3027]
sync_up = [8077, 8077, 8077, 8077, 8077, 8077]
sync_smp = [19430, 19430, 19430, 19430, 19430, 19430]
async_up = [10559, 5988, 3473, 2520, 1977, 1722]
async_smp = [10359, 4570, 2288, 1863, 1567, 1477]

server_up = [1, 0.5, 0.2501, 0.1254, 0.0627, 0.0318]
client_up = [1, 0.5, 0.2504, 0.1253, 0.0628, 0.032]
server_smp = [1, 0.5006, 0.2513, 0.2217, 0.1762, 0.1685]
client_smp = [1, 0.5011, 0.2513, 0.1274, 0.0659, 0.0359]

# plt.subplot(121)
x = np.arange(len(labels))  # x轴刻度标签位置
width = 0.18  # 柱子的宽度
# 计算每个柱子在x轴上的位置，保证x轴刻度标签居中
plt.bar(x - 2 *width, sync_up_fp, width, label='sync-up-fp', color = "black", edgecolor='black')
plt.bar(x - 1 * width, sync_up, width, label='sync-up', color='dimgray', edgecolor='black')
plt.bar(x, sync_smp, width, label='sync-smp', color="darkgray", edgecolor='black')
plt.bar(x + 1 * width, async_up, width, label='async-up', color="gainsboro", edgecolor='black')
plt.bar(x + 2 * width, async_smp, width, label='async-smp', color="white", edgecolor='black')
plt.ylabel('The average CPU cycles used by a single IPC')
plt.xlabel('concurrency')
# x轴刻度标签位置不进行计算
plt.xticks(x, labels=labels)
plt.legend(loc="upper left")

ax2 = plt.twinx()
ax2.set_ylabel("U-notification frequency(uintr count/ipc count)")
ax2.set_ylim([0, 1])
plt.plot(labels, server_up, marker='.', c='black', ms=5, linewidth='1', label="server-up")
plt.plot(labels, server_smp, marker='.', c='black', linestyle='--', ms=5, linewidth='1', label="server-smp")
plt.legend(loc="upper right")

# ax3 = plt.subplot(122)
# labels = ['0', '10 * 10', '20 * 20', '30 * 30']
# concurrency_8 = [0.2217, 0.1764, 0.1127, 0]
# concurrency_16 = [0.1762, 0.1303, 0.0764, 0]
# concurrency_32 = [0.1685, 0.0981, 0, 0]
# # ax3.yaxis.set_label("uintr count/ipc count")
# ax3.set_ylabel("uintr count/ipc count")
# plt.ylim([0, 0.3])

# plt.xlabel('matrix size')
# plt.title('(2) U-notificaton frequency')
# plt.plot(labels, concurrency_8, "r", marker='.', c='black', ms=5, linewidth='1', label="concurrency 8")
# plt.plot(labels, concurrency_16, "r", marker='.', c='darkseagreen', ms=5, linewidth='1', label="concurrency 16")
# plt.plot(labels, concurrency_32, "r", marker='.', c='steelblue', ms=5, linewidth='1', label="concurrency 32")
# plt.legend(loc="upper right")
# plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.25, hspace=0.35)
# # plt.show()
plt.savefig("ipc_test.svg")