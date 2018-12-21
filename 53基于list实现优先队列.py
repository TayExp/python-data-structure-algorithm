class PrioQueueError(ValueError):
    """定义一个异常类在优先队列类里使用"""
    pass

class PrioQue:
    def __init__(self,elist=[]):
        self._elems = list(elist)
        self._elems.sort(reverse=True)

    def enqueue(self,e):
        i = len(self._elems)-1
        while i >= 0:
            if self._elems[i] >= e:
                self._elems.insert(i+1, e)
                break
            i -= 1

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError("in peek")
        return self._elems[-1]

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError
        return self._elems.pop("in dequeue")
