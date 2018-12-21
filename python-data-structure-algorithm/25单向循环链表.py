
class Node(object):
    """节点"""
    def __init__(self,elem):
        self.elem = elem
        self.next = None

class SingleCycleLinkList(object):
    """单链表"""
    def __init__(self,node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        cur = self.__head.next
        count = 1
        while cur != self.__head:
            count = count+1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem," ")#python空格代替\n
            cur = cur.next
        print(cur.elem," ")

    def add(self,item):
        """头部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            node.next = self.__head
            self.__head = node
            cur = node.next
            while cur.next!=node.next:
                cur = cur.next
            cur.next = node

    def append(self,item):
        """尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

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
        if self.is_empty():
            return False
        pre = self.__head
        # 先判断是否为头结点
        if pre.elem == item:
            if pre.next == pre:#只有一个节点
                self.__head = None
            else:
                while pre.next != self.__head:
                    pre = pre.next
                self.__head = self.__head.next
                pre.next = self.__head
            return True
        while pre.next != self.__head:
            if pre.next.elem == item:
                pre.next = pre.next.next
                return True
            pre = pre.next
        #最后一个节点，且非头结点
        if pre.next.elem == item:
            pre.next = self.__head
            return True
        return False


    def search(self,item):
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        if cur.elem == item:
            return True
        return False

if __name__ == '__main__':
    ll = SingleCycleLinkList()
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
    print(ll.search(7))
    print("-"*10)
    ll.remove(1)
    ll.remove(7)
    ll.remove(3)
    ll.travel()

    print(ll.search(7))
    print(ll.search(8))
    print("length of list is %d"%ll.length())