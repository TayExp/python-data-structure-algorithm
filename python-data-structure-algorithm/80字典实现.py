from collections.abc import Iterable

class Assoc:
    def __init__(self, key, value):
        self.key = key
        self.value =value
    def __lt__(self, other):
        return self.key < other.key
    def __le__(self, other):
        return self.key < other.key or self.key == other.key
    def __str__(self):
        return "Assoc({0},{1})".format(self.key,self.value)

class DictList:
    """字典的线性表实现"""
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return not self._elems

    def num(self):
        return len(self._elems)

    def search(self,key):
        for asso in self._elems:
            if asso.key == key:
                return asso.value
        else:
            return False

    def insert(self,key,value):
        self._elems.append(Assoc(key,value))

    def delete(self,key):
        for i in range(len(self._elems)):
            if self._elems[i].key == key:
                self._elems.pop(i)
                break
        else:
            return False

    def values(self):
        """支持以迭代方式获得值"""
        value = []
        for entry in self._elems:
            value.append(entry.value)
        return MyList(value)

    def entries(self):
        """支持以迭代方式获得二元组"""
        return MyList(self._elems)

class MyList(object):
    """自定义一个可迭代对象"""
    def __init__(self,elems):
        self.items = list(elems)
    def __iter__(self):#
        return MyIterator(self)
class MyIterator(object):
    """自定义的供上面可迭代对象使用的一个迭代器"""
    def __init__(self,mylist):
        self.mylist = mylist
        self.current = len(self.mylist.items)#记录当前访问的位置

    def __next__(self):
        if self.current > 0:
            item = self.mylist.items[self.current-1]
            self.current -= 1
            return item
        else:
            raise StopIteration

# dic = DictList()
# dic.insert(1,"a")
# dic.insert(2,"b")
# dic.insert(3,"c")
# dic.insert(4,"d")
# dic.insert(6,"f")
# for i in dic.entries():
#     print(i)
# for v in dic.values():
#     print(v)
# dic.delete(3)
# for i in dic.entries():
#     print(i)

class DictOrdList(DictList):
    """有序线性表"""
    @staticmethod
    def bisearch(lst,key):
        low, high = 0, len(lst)-1
        while low <= high:
            mid = low + (high-low)//2
            if lst[mid].key < key:
                high = mid - 1
            elif lst[mid].key > key:
                low = mid + 1
            else:
                return mid
        return low

    def search(self,key):
        if self.is_empty():
            return False
        index = self.bisearch(self._elems,key)
        if self._elems[index].key == key:
            return self._elems[index].value
        else:
            return False

    def insert(self,key,value):
        index = self.bisearch(self._elems,key)
        if self.is_empty():
            self._elems.append(Assoc(key,value))
        else:
            self._elems.insert(index,Assoc(key,value))

    def delete(self,key):
        if self.is_empty():
            return False
        index = self.bisearch(self._elems, key)
        if self._elems[index].key == key:
            return self._elems.pop(index)
        else:
            return False


dic = DictOrdList()
dic.insert(1,"a")
dic.insert(6,"b")
dic.insert(3,"c")
dic.insert(7,"d")
dic.insert(10,"f")
dic.insert(5,"f")
dic.insert(3,"f")
for i in dic.entries():
    print(i)
for v in dic.values():
    print(v)
dic.delete(3)
for i in dic.entries():
    print(i)