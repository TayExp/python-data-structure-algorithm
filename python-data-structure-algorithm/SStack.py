class StackUnderflow(ValueError):
    pass

class Sstack():
    """基于顺序表实现的栈"""
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self._elems == []:
            raise StackUnderflow("in Sstack.peek.")
        return self._elems[-1]

    def push(self,elem):
        self._elems.append(elem)

    def pop(self):
        if self._elems == []:
            raise StackUnderflow("in Sstack.pop().")
        return self._elems.pop()