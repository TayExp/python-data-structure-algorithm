from multiprocessing import Pool,freeze_support
import os,time,random
#freeze_support()"冻结"时生成 Windows 可执行文件
        #原因是Windows没有直接的fork()
        #Window是通过创建一个新的过程代码,在子进程运行来模拟fork()
        #由于代码是在技术无关的进程中运行的，所以它必须在运行之前交付
        #它传递的方式首先是被pickle，然后通过管道从原始进程发送到新进程
        #另外，这个新进程被告知它必须运行通过管道传递的代码通过传递
        #freeze_support() 函数的任务是检查它正在运行的进程是否应该通过管道或不运行代码。
def worker(msg):
    t_start = time.time()
    print("%s开始执行，进程号为%d" %(msg,os.getpid()))
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,"执行完毕，耗时%.2f" % (t_stop-t_start))


def main():
    #定义一个进程池，最大进程数3
    po = Pool(3)
    for i in range(10):
        # Pool().apply_async(要调用的目标,(传递给目标的参数元祖,))
        # 每次用空闲的子进程调用目标
        po.apply_async(worker,(str(i),))
    print("----start----")
    po.close()
    ####
    # 关闭等待po中所有子进程执行完成，主进程堵塞
    # 必须放在close或terminate语句后面
    po.join()
    print("----end----")

#    由于Python运行过程中，新创建进程后，进程会导入正在运行的文件，即在运行代码0.1 的时候，
    # 代码在运行到mp.Process时，新的进程会重新读入改代码，对于没有if __name__ == "__main__"
    # 保护的代码，新进程都认为是要再次运行的代码，这是子进程又一次运行mp.Process，
# 但是在multiprocessing.Process的源码中是对子进程再次产生子进程是做了限制的，是不允许的，于是出现如上的错误提示
if __name__ == '__main__':
    freeze_support()
    main()