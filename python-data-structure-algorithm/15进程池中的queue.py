# 多个子进程间的通信
# 不是multiprocessing.Queue()
# Queue objects only shared between process through inherictance
# 而进程池中的进程并不是由当前同一个父进程创建的原因
# 使用multiprocess的manager类
# magager返回的manager对象控制了一个server进程，可用于多进程之间的安全通信
# 支持list,dict,Namespace,Lock,RLock,Semaphore,BoundedSemaphore,Condition,Event,Queue,Value和Array
from multiprocessing import Pool,Manager
import os,time,random

def reader(q):
    print("reader启动（%s),父进程为%s"%(os.getpid(),os.getppid()))
    for i in range(q.qsize()):
        print("reader从Queue获取到消息：%s" % q.get(True))

def writer(q):
    print("writer启动（%s),父进程为%s"%(os.getpid(),os.getppid()))
    # for i in range ("hello, world!"):
    for i in "hello,world!":
        q.put(i)

if __name__ == '__main__':
    print("(%s)主进程start"%os.getpid())
    q = Manager().Queue()
    po = Pool()
    po.apply_async(writer,(q,))

    time.sleep(1)

    po.apply_async(reader,(q,))
    po.close()
    po.join()
    print("(%s)主进程End"%os.getpid())

