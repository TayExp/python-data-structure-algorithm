#线程是对全局变量随意遂改可能造成多线程之间对全局变量的混乱（即线程非安全）
# 在一个进程内的所有线程共享全局变量，很方便在多个线程间共享数据
import threading
import time
# 全局变量
g_num = 100
g_list = [11,22,33]
def work1(nums = [0]):
    global g_num
    for i in range(3):
        g_num+=1
    nums.append(44)
    print("----in work1, g_num is %d,\n nums = " %g_num, nums)



def work2():
    global g_num
    print("----in work2, g_num is %d,\n nums = " % g_num, g_list)


print("------创建线程之前，g_num = %d, g_lsit=" %g_num, g_list)

t1 = threading.Thread(target=work1, args=(g_list,))# 有个逗号
t1.start()

#让线程1做完事情
time.sleep(1)

t2 = threading.Thread(target=work2)
t2.start()

# 列表当作实参传递到线程中
#如果多个线程同时对同一个全局变量操作，会出现资源竞争问题，从而数据结果会不正确