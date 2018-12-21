from timeit import Timer

def t1():
    li = []
    for i in range(10000):
        li.append(i)

def t2():#重新建一个列表
    li =[]
    for i in range(10000):
        li += [i]

def t3():
    li = [i for i in range(10000)]

def t4():# list转换
    # python2返回列表，python3返回可迭代对象
    li = list(range(10000))

def t5():
    li = []
    for i in range(10000):
        li.extend([i])
#insert(0,i)
#pop(0) pop()
#存储方式不同
timer1 = Timer("t1()", "from __main__ import t1")#所执行的代码、设置、
print("append:", timer1.timeit(1000))#测算1000次，返回秒数

timer2 = Timer("t2()", "from __main__ import t2")#所执行的代码、设置、
print("+:", timer2.timeit(1000))#测算1000次，返回秒数

timer3 = Timer("t3()", "from __main__ import t3")#所执行的代码、设置、
print("i for i in range:", timer3.timeit(1000))#测算1000次，返回秒数

timer4 = Timer("t4()", "from __main__ import t4")#所执行的代码、设置、
print("list(range()):", timer4.timeit(1000))#测算1000次，返回秒数

timer5 = Timer("t5()", "from __main__ import t5")#所执行的代码、设置、
print("extend:", timer5.timeit(1000))#测算1000次，返回秒数
# append: 9.373077641
# +: 10.811997487000001
# i for i in range: 5.302071258000002
# list(range()): 3.279342767000003