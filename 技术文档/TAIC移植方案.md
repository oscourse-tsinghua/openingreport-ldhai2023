## 1. 背景
当前基于用户态中断的ReL4存在一定的性能问题：
- 在低并发场景下，由于频繁的用户态中断以及异步任务额外的入队出队开销，导致性能比同步低。
- 在高并发场景下，异步任务的运行时开销（fetch、wake等高频操作）成为主要的性能瓶颈。
## 2. TAIC
提供了两套解决方案。
- 异步通知，比TKF的用户态中断快20+个cycles
- 硬件队列：使用硬件队列存储任务号，用硬件加速fetch、wake等高频操作。

## 3. 适配方案

### 3.1 异步通知
由于TAIC移除了用户态中断的原有实现，因此需要重新适配TAIC的异步通知机制。TAIC的接口需要程序能够直接访问对应硬件的端口。每个队列的端口被分配到单独的页地址上。

ReL4需要用户态直接调用异步通知，并且操作硬件队列，因此需要借助内核将对应的端口页映射到地址空间中。

几个可以预见的适配点：
- notification内核对象存储队列绑定的os_id, process_id。
- register_receiver传递notification cap以及handler两个参数，陷入内核态进行注册（需要映射队列地址），返回sender_os和sender_process并缓存到用户态。
	- 重新注册接收端，每次唤醒接收端后需要重新注册，此时直接从上一次的sender_os和sender_process。
- register_sender传递notification cap，陷入内核态映射队列地址，返回recv_os和recv_process（存储在notification内核对象中）。

## 3.2 任务队列
使用TAIC的LocalQueue来实现任务队列。LocalQueue对每个进程分配了8个任务队列，从硬件的角度来看没有优先级的区分，队列之间进行了负载均衡。

ReL4需要支持优先级的任务队列，由于引入了负载均衡，可能需要对优先级进行详细设计。

## 3.3 任务唤醒

- 跨进程的任务唤醒：TAIC目前仅支持同一个进程每次阻塞在异步通知上的协程只有一个，因此应用于ReL4中的dispatch协程，dispatch协程被跨进程的异步信号唤醒，并读取共享内存中的数据，然后唤醒之前阻塞的worker协程。
- 进程内部的任务唤醒：进程内部的worker协程唤醒由dispatcher协程代理，dispatcher协程会调用LocalQueue.enqueue()将任务加入到就绪队列中。
