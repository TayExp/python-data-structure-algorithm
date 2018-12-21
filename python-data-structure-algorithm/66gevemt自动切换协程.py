#当一个greenlet遇到IO(指的是input output 输入输出，
# 比如网络、文件操作等)操作时，比如访问网络，
# 就自动切换到其他的greenlet，
# 等到IO操作完成，再在适当的时候切换回来继续执行。

import gevent
import random
import time
from gevent import monkey
# def f(n):
#     for i in range(n):
#         print(gevent.getcurrent(),i)
#         gevent.sleep(1)#模拟一个耗时操作
#
# g1 = gevent.spawn(f,5)
# g2 = gevent.spawn(f,5)
# g3 = gevent.spawn(f,5)
# g1.join()
# g2.join()
# g3.join()
monkey.patch_all()
# 将程序中用到的耗时操作的代码，换为gevent中自己实现的模块
def coroutine_work(coroutine_name):
    for i in range(10):
        print(coroutine_name,i)
        time.sleep(random.random())
gevent.joinall([gevent.spawn(coroutine_work, "work1"), gevent.spawn(coroutine_work,"work2")])
