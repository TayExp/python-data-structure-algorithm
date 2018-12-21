import threading
import time

g_num = 0

def work1(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("----in work1, g_num is %d---"%g_num)


def work2(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("----in work2, g_num is %d---"%g_num)


print("---线程创建之前g_num is %d---"%g_num)

t1 = threading.Thread(target=work1, args=(1000000,))
t1.start()

t2 = threading.Thread(target=work2, args=(1000000,))
t2.start()

# while len(threading.enumerate()) != 1:
#     time.sleep(1)

print("2个线程对同一个全局变量操作之后的最终结果是:%s" % g_num)
# 如果多个线程同时对同一个全局变量操作，会出现资源竞争问题，从而数据结果会不正确
# 线程同步：线程在对g_num进行修改时，都要先上锁，处理完后再解锁，
# 在上锁的整个过程中不允许其他线程访问，就保证了数据的正确性
# 在线程间共享多个资源的时候，
# 如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁。