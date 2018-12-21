class PrioQueueError(ValueError):
    """定义一个异常类在优先队列类里使用"""
    pass

class PrioQueue:
    """implementing priority queue using heaps
    基于小顶堆实现优先队列"""
    def __init__(self,enlist=[]):
        self._elems = list(enlist)
        if self._elems:
            self.buildheap()

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError("in peek")
        return self._elems[0]

    def enqueue(self,e):
        self._elems.append(None)
        # 向上筛选一次
        self.siftup(e, len(self._elems)-1)
    def siftup(self, e, last):
        """
        :param e: 要加入的元素
        :param last: 原堆的列表append(None)之后的len-1, 即e的最初位置
        """
        i, j = last, (last-1)//2 # e和其父节点的索引
        while i>0 and self._elems[j] > e:
            self._elems[i] = self._elems[j]
            i, j = j, (j-1)//2
        self._elems[i] = e

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError("in enqueue")
        e0 = self._elems[0]
        e = self._elems.pop() # 从原堆最后取出一个元素，将这个元素放入堆顶
        if len(self._elems) > 0: #取出后不空
            self.siftdown(e, 0, len(self._elems))
        return e0
    def siftdown(self,e,begin,end):
        """
        向下筛选
        :param e: 要插入的元素，原堆尾元素
        :param begin: 堆顶开始，0
        :param end: 所有索引应<end
        """
        elems, i, j = self._elems, begin, begin*2+1
        while j < end:
            if j+1 < end and elems[j+1] < elems[j]:
                j += 1
            # 三个数据，e最小，找到了合适的位置
            if e < elems[j]:
                break
            elems[i] = elems[j] #elems[j]最小，上移
            i, j = j, j * 2 + 1
        elems[i] = e

    def buildheap(self):
        end = len(self._elems)
        for i in range(end//2,-1,-1): # 从最右最下分支节点到堆顶逐一建堆
            self.siftdown(self._elems[i],i,end)

    def __str__(self):
        return str(self._elems)


def main():
    heap = PrioQueue([3,40,53,28,81,10,44,59,60,2])
    print(heap)
    heap.enqueue(7)
    print(heap)
    heap.dequeue()
    print(heap)
    while not heap.is_empty():
        print(heap.dequeue())


if __name__ == '__main__':
    main()