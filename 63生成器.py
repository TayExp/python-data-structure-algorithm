# 第一种方法

G = (x*2 for x in range(5))
print(G)

# print(next(G))
# print(next(G))
# print(next(G))
# print(next(G))
# print(next(G))
# print(next(G))


# 创建生成器第二种方法


# 斐波那契数列迭代器
def fib(n):
    current = 0
    num1,num2 = 0,1
    while current<n:
        num = num1
        num1,num2 = num2,num1+num2
        current += 1
        yield num# 存在yield关键字，是生成器
    return "done"# python2不允许在生成器函数中使用return

for i in fib(5):
    print(i)


# 拿到generator的return语句的返回值
G = fib(5)
while True:
    try:
        print(G.__next__())
    except StopIteration as e:
        print("生成器返回值：%s" %e.value)
        break
print("-"*20)
def gen(value):
    i = 0
    while i<6:
        new = (yield value)
        #传进去的值是send里的参数的即这里的yield value,同时函数暂停返回value值
        value = new
        i+=1
f = gen("H")
# print(next(f))
print(f.send(None))# just started,必须是None参数
print(f.send("h"), f.send("e"), f.send("l"),f.send("l"), f.send("o"))
# f.send("w")