class Node(object):
    """节点"""
    def __init__(self,elem):
        self.elem = elem
        self.next = None
        self.prev = None

class DoubleLinkList(object):
    """双链表"""
    def __init__(self,node=None):
        self.__head = node

    def is_empty(self):
        return self.__head is None

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
        self.__head.prev = node
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
            node.prev = cur

    def insert(self,pos,item):
        """指定位置添加元素
        :param pos: 从0开始
        """
        if pos <= 0:
            self.add(item)
        elif pos >(self.length()-1):
            self.append(item)
        else:
            cur = self.__head
            count = 0
            while count < pos:
                cur = cur.next
                count = count + 1

            node = Node(item)

            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self,item):
        """删除一个元素"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
            # 先判断是否为头结点
                if cur == self.__head:
                    self.__head = self.__head.next
                    # 如果此时头结点不为空
                    if self.__head:
                        self.__head.prev = None
                else:
                    cur.prev.next = cur.next
                    #如果此时下个节点不为空
                    if cur.next:
                        cur.next.prev = cur.prev
                #cur节点还是cur节点，但没人能管它了？？应该回收一下么，del cur
                return True
            else:
                cur = cur.next
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
    ll = DoubleLinkList()
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
    print("length of list is %d" % ll.length())
    print("-"*10)
    ll.remove(1)
    ll.remove(7)
    ll.remove(3)
    ll.travel()

    print(ll.search(7))
    print(ll.search(8))
    print("length of list is %d"%ll.length())