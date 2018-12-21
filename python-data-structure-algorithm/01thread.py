# 并发：指的是任务数多余cpu核数，通过操作系统的各种任务调度算法，实现用多个任务“一起”执行（实际上总有一些任务不在执行，因为切换任务的速度相当快，看上去一起执行而已）
# 并行：指的是任务数小于等于cpu核数，即任务真的是一起执行的
import time
import threading
# threading模块能完成多任务的程序开发
def task1():
    for i in range(3):
        print("run task1...")
        time.sleep(1)

def task2():
    for i in range(3):
        print("run task2...")
        time.sleep(1)

def task3():
    for i in range(3):
        print("run task3...|")
        time.sleep(1)


if __name__ == '__main__':
    print("start--%s" %time.ctime())
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t3 = threading.Thread(target=task3)
    t1.start()
    t2.start()
    t3.start()
    # 查看线程数量
    while True:
        length = len(threading.enumerate())
        print("the number of threadings is %d" %length)
        if length<=1:
            break
        time.sleep(0.5)

    # 主线程会等待所有的子线程结束后才结束
    time.sleep(5)
    print("over--%s" % time.ctime())


