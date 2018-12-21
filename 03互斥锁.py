import time
import threading
# 线程同步能够保证多个线程安全访问竞争资源，最简单的同步机制是引入互斥锁
# 某个线程要更改共享数据时，先将其锁定，此时资源的状态为“锁定”，其他线程不能更改；直到该线程释放资源，将资源的状态变成“非锁定”，其他的线程才能再次锁定该资源某个线程要更改共享数据时，先将其锁定，此时资源的状态为“锁定”，其他线程不能更改；直到该线程释放资源，
# 将资源的状态变成“非锁定”，其他的线程才能再次锁定该资源
# 互斥锁保证了每次只有一个线程进行写入操作，从而保证了多线程情况下数据的正确性。
g_num = 0

def work1(num):
    global g_num

    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("----in work1, g_num is %d---"%g_num)


def work2(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("----in work2, g_num is %d---"%g_num)


print("---线程创建之前g_num is %d---"%g_num)
# 创建一个互斥锁 默认是未上锁状态
mutex = threading.Lock()
t1 = threading.Thread(target=work1, args=(1000000,))
t1.start()

t2 = threading.Thread(target=work2, args=(1000000,))
t2.start()

while len(threading.enumerate()) != 1:
    time.sleep(1)
print("2个线程对同一个全局变量操作之后的最终结果是:%s" % g_num)


# 如果这个锁之前是没有上锁的，那么acquire不会堵塞,否则堵塞直到解锁
