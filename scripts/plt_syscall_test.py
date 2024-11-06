import matplotlib.pyplot as plt
import numpy as np

plt.rc('font', family='Times New Roman')
plt.figure(figsize=(8, 5))
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
plt.bar(x - 1 * width, sync, width, label='sync', color="darkseagreen")
plt.bar(x, async_up, width, label='async-up', color="steelblue")
plt.bar(x + 1 * width, async_smp, width, label='async-smp', color="brown")
plt.ylabel('cycles')
plt.xlabel('concurrency')
plt.title('Average number of cycles per request')
# x轴刻度标签位置不进行计算
plt.xticks(x, labels=labels)
plt.legend(loc="upper left")

ax2 = plt.twinx()
ax2.set_ylabel("S-trap frequency(trap count / syscall count)")
ax2.set_ylim([0, 0.15])
plt.plot(labels, server_up, "r", marker='.', c='r', ms=5, linewidth='1', label="server-up")
plt.plot(labels, server_smp, "r", marker='.', c='b', ms=5, linewidth='1', label="server-smp")
plt.legend(loc="upper right")

# plt.show()
plt.savefig("syscall_test.png")