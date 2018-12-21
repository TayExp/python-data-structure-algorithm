# ############### 定义 ###############
class Goods:
    """python3中默认继承object类
        以python2、3执行此程序的结果不同，因为只有在python3中才有@xxx.setter  @xxx.deleter
    """
    def __init__(self):
        self.original_price = 100
        self.discount = 0.8

    def get_price(self):
        return self.original_price*self.discount

    def set_price(self, value):
        self.original_price = value

    def del_price(self):
        del self.original_price
    PRICE = property(get_price, set_price, del_price, "描述字符串...")

# ############### 调用 ###############
obj = Goods()
obj.PRICE          # 自动调用第一个参数中定义的方法：get_xxx
obj.PRICE = 123    # 自动调用第二个参数中定义的方法:set_xxx
print(obj.PRICE, "-"*50)
print(Goods.PRICE.__doc__) # 自动获取第四个参数中设置的值：description...
del obj.PRICE      # 自动调用第三个参数中定义的方法:del_xxx
# 已经没有obj.price了


