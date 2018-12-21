# 两个子进程：一个忘Queue里写数据，应该从Queue里读数据
from multiprocessing import  Process, Queue
import os, time, random

def download_from_wed(q):
    """模拟下载数据"""
    data = [11,22,33,44,5,6,7,8,9,10,1,2,3,4]
    for value in data:
        print("put %d to queue" % value)
        q.put(value)
        time.sleep(random.random())
def analysis_data(q):
    """数据处理"""
    while True:
        if not q.empty():
            value = q.get(True)
            print("get %d from queue" % value)
            time.sleep(random.random())
        else:
            break
def main():
    q = Queue()

    pw = Process(target=download_from_wed, args=(q,))
    pr = Process(target=analysis_data, args=(q,))
    pw.start()
    pw.join()
    pr.start()
    pr.join()
    print("")
    print("完成")

if __name__ == '__main__':
    main()