import matplotlib.pyplot as plt
import numpy as np

plt.rc('font', family='Times New Roman')
plt.figure(figsize=(8, 4))
# 构造x轴刻度标签、数据
labels = ['1', '2', '4', '8', '16', '32']
sync_up = [527, 839, 821, 779, 699, 577]
sync_smp = [760, 755, 748, 714, 642, 539]
async_up = [1021, 1333, 1550, 1717, 1574, 1272]
async_smp = [1416, 2038, 2091, 2087, 1891, 1421]

sync_up_ms = [1.89, 2.37, 4.85, 10.21, 22.72, 54.61]
sync_smp_ms = [1.31, 2.63, 5.33, 11.14, 24.77, 58.63]
async_up_ms = [0.97, 1.48, 2.55, 4.58, 9.86, 23.84]
async_smp_ms = [0.7, 0.97, 1.89, 3.81, 8.39, 22.2]


x = np.arange(len(labels))  # x轴刻度标签位置
width = 0.2  # 柱子的宽度
# 计算每个柱子在x轴上的位置，保证x轴刻度标签居中
plt.bar(x - 1.5 *width, sync_up, width, label='sync-up', color="black")
plt.bar(x - 0.5 * width, sync_smp, width, label='sync-smp', color="darkseagreen")
plt.bar(x + 0.5 * width, async_up, width, label='async-up', color="steelblue")
plt.bar(x + 1.5 * width, async_smp, width, label='async-smp', color="brown")

plt.ylabel('throughput(pps)')
plt.xlabel('connection nums')
plt.title('TCP server throughput')
# x轴刻度标签位置不进行计算
plt.xticks(x, labels=labels)
plt.legend(loc="upper left")

ax2 = plt.twinx()
ax2.set_ylabel("delay(ms)")
ax2.set_ylim([0, 60])
plt.plot(labels, sync_up_ms, "r", marker='.', c='r', ms=5, linewidth='1', label="sync-up")
plt.plot(labels, sync_smp_ms, "r", marker='.', c='b', ms=5, linewidth='1', label="sync-smp")
plt.plot(labels, async_up_ms, "r", marker='.', c='magenta', ms=5, linewidth='1', label="async-up")
plt.plot(labels, async_smp_ms, "r", marker='.', c='lawngreen', ms=5, linewidth='1', label="async-smp")
plt.legend(loc="upper right")


# plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.2, hspace=0.35)
# plt.show()
plt.savefig("tcp_test.png")