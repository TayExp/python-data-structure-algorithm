class FibIterator(object):
    """斐波那契数列迭代器"""
    def __init__(self,n):
        """
        :param n: int,指明生成数列前n个数
        """
        self.n = n
        self.current = 0
        self.num1 = 0
        self.num2 = 1

    def __next__(self):
        """被next()函数调用，获取下一个数"""
        if self.current < self.n:
            num = self.num1
            self.num1, self.num2 =self.num2,self.num2+self.num1
            self.current += 1
            return num
        else:
            raise StopIteration

    def __iter__(self):
        """迭代器的iter返回自身即可"""
        return self
if __name__ == '__main__':
    fib = FibIterator(10)
    for num in fib:
        print(num)
    print("-"*10)
    # 不是转换，而是迭代一个一个生成和加入
    print(list(FibIterator(15)))

    print(tuple(FibIterator(20)))
