import threading
import time

class MyThread(threading.Thread):
    #Thread类有一个run方法，用于定义线程的功能函数
    #当该线程获得执行的机会时，就会调用run方法执行线程
    #当线程的run()方法结束时该线程完成
    def run(self):
        for i in range(3):
            time.sleep(1)#（Blocked）
            #就绪（Runnable）
            msg = "I'm "+self.name+" @ "+str(i)
            print(msg)

def wtest():
    # 5个线程，多线程程序的执行顺序是不确定的
    for i in range(5):
        t = MyThread()
        t.start()

if __name__ == '__main__':
    wtest()
