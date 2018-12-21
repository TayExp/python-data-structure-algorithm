# 创建进程
# 使用多进程实现多任务
import time
import multiprocessing
import os
def task1():
    print('子进程运行中，pid=%d...' % os.getpid())
    # os.getpid获取当前进程的进程号
    for i in range(3):
        print("run task1...")
        time.sleep(1)

def task2():
    print('子进程运行中，pid=%d...' % os.getpid())
    for i in range(3):
        print("run task2...")
        time.sleep(1)

def task3():
    print('子进程运行中，pid=%d...' % os.getpid())
    for i in range(3):
        print("run task3...|")
        time.sleep(1)


if __name__ == '__main__':
    print("start--%s" %time.ctime())
    print('父进程pid: %d' % os.getpid())
    # os.getpid获取当前进程的进程号
    t1 = multiprocessing.Process(target=task1)
    t2 = multiprocessing.Process(target=task2)
    t3 = multiprocessing.Process(target=task3)
    t1.start()
    t2.start()
    t3.start()
    # 查看线程数量
    # 主线程会等待所有的子线程结束后才结束
    time.sleep(5)
    print("over--%s" % time.ctime())


