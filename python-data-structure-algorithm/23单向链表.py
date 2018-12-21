
class Node(object):
    """节点"""
    def __init__(self,elem):
        self.elem = elem
        self.next = None

class SingleLinkList(object):
    """单链表"""
    def __init__(self,node=None):
        self.__head = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        """链表长度"""
        cur = self.__head
        count = 0
        while cur != None:
            count = count+1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            print(cur.elem," ")#python空格代替\n
            cur = cur.next

    def add(self,item):
        """头部添加元素"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self,item):
        """尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self,pos,item):
        """指定位置添加元素
        :param pos: 从0开始
        """
        if pos <= 0:
            self.add(item)
        elif pos >(self.length()-1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < pos-1:
                pre = pre.next
                count = count + 1
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self,item):
        """删除一个元素"""
        # 先判断是否为头结点
        if self.__head.elem == item:
            self.__head = self.__head.next
            return True
        pre = self.__head
        while pre.next != None:
            if pre.next.elem == item:
                pre.next = pre.next.next
                return True
            else:
                pre = pre.next
        return False

    def search(self,item):
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

if __name__ == '__main__':
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.search(1))
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(6)
    ll.append(7)
    ll.add(1)
    ll.insert(4,5)
    ll.travel()
    print("-"*10)
    ll.remove(1)
    ll.remove(7)
    ll.remove(3)
    ll.travel()

    print(ll.search(7))
    print(ll.search(8))
    print("length of list is %d"%ll.length())