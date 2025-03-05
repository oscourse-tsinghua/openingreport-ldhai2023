import matplotlib.pyplot as plt
import numpy as np

plt.rc('font',family='Times New Roman')
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

x = ["ntfn-up", "U-ntfn-up", "ntfn-smp", "U-ntfn-smp"]
# 
context_switch = [3405 ,2001, 3506, 2030]
page_table_switch = [6044, 0, 6157, 0]
hw_interrupt = [0, 2733, 10029, 2655]

plt.subplot(121)
plt.bar(x, context_switch,width=0.4,label='context switch',color='black',edgecolor='grey',zorder=5)
plt.bar(x, page_table_switch,width=0.4,bottom=context_switch,label='page table switch',color='dimgray',edgecolor='grey',zorder=5)
plt.bar(x, hw_interrupt,width=0.4,bottom=[x + y for x, y in zip(context_switch, page_table_switch)],label='hardware cost',color='white',edgecolor='grey',zorder=5)
plt.tick_params(axis='x',length=0)
plt.ylabel('CPU cycles')
plt.legend(loc="upper left")



labels = ['Interrupt', 'Polling', 'Hybrid polling']
lantency = [10559, 6968, 8172]
CPU_utilization = [0.97, 0.57, 0.92]
width = 0.4  # 柱子的宽度
x = np.arange(len(labels))  # x轴刻度标签位置
ax2 = plt.subplot(122)

bar1 = ax2.bar(x - width / 2, lantency, width, label='lantency', color = "black", edgecolor='black')
ax2.set_ylabel("lantency(cpu cycles)")
plt.xticks(x, labels=labels)
ax3 = ax2.twinx()
ax3.set_ylabel("CPU Utilization")
ax3.set_ylim([0.5, 1])
bar2 = ax3.bar(x + width / 2, CPU_utilization, width, label='CPU utilization', color = "grey", edgecolor='black')

handler = [bar1, bar2]
handler_label = [bar1.get_label(), bar2.get_label()]
ax3.legend(handler, handler_label, loc='upper right')



plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.35, hspace=0.35)

# fig.legend(loc='upper left', bbox_to_anchor=(0.1, 1))
plt.savefig('ntfn_test.svg')