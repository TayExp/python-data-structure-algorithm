from collections.abc import Iterable
class MyList(object):
    """自定义一个可迭代对象"""
    def __init__(self):
        self.items = list()

    def add(self,name):
        self.items.append(name)
    def __iter__(self):#
        return MyIterator(self)

class MyIterator(object):
    """自定义的供上面可迭代对象使用的一个迭代器"""
    def __init__(self,mylist):
        self.mylist = mylist
        self.current = 0#记录当前访问的位置
    # def __iter__(self):
    #     # return self
    #     pass
    def __next__(self):
        if self.current < len(self.mylist.items):
            item = self.mylist.items[self.current]
            self.current += 1
            return item
        else:
            raise StopIteration
# 判断*obj是否可以迭代
# 调用iter函数得到__iter__方法的返回值(一个迭代器)
# for 循环一次，调用一下迭代器的next()方法

cm = MyList()
print(isinstance(cm,Iterable))

cm.add("aa")
cm.add("bb")
cm.add("cc")
for name in cm:
    print(name)