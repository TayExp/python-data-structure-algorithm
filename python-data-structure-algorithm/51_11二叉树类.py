class BinTNode:
    """二叉树结点"""
    def __init__(self, dat, left=None, right=None):
        self.data = dat
        self.left = left
        self.right = right
from SStack import *
class BinTree:
    """二叉树类"""
    def __init__(self):
        self._root = None

    def is_empty(self):
        return not self._root

    def leftchild(self):
        return self._root.left

    def rightchild(self):
        return self._root.right

    def set_root(self,rootnode):
        self._root = rootnode

    def set_left(self,leftchild):
        self._root.left = leftchild

    def set_right(self,rightchild):
        self._root.right = rightchild

    def pre_order_elements(self):
        t, s = self._root, Sstack()
        while t is not None or not s.is_empty():
            while t is not None:
                s.push(t.right)
                yield t.data
                t = t.left
            t = s.pop()