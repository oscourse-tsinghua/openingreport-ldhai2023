import matplotlib.pyplot as plt

plt.rc('font',family='Times New Roman')
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

x = ["notifcation-up", "U-notification-up", "notification-smp", "U-notification-smp"]
# 
context_switch = [3405 ,2001, 3506, 2030]
page_table_switch = [6044, 0, 6157, 0]
hw_interrupt = [0, 2733, 10029, 2655]

plt.bar(x, context_switch,width=0.4,label='context switch',color='black',edgecolor='grey',zorder=5)
plt.bar(x, page_table_switch,width=0.4,bottom=context_switch,label='page table switch',color='dimgray',edgecolor='grey',zorder=5)
plt.bar(x, hw_interrupt,width=0.4,bottom=[x + y for x, y in zip(context_switch, page_table_switch)],label='hardware cost',color='white',edgecolor='grey',zorder=5)
plt.tick_params(axis='x',length=0)
plt.xlabel('Experimental Parameters')
plt.ylabel('CPU cycles')
plt.legend(loc="upper left")
plt.savefig('ntfn_test.svg')