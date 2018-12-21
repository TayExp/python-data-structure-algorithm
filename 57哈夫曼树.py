class BinTNode:
    """二叉树结点"""
    def __init__(self, dat, left=None, right=None):
        self.data = dat
        self.left = left
        self.right = right

class HTNode(BinTNode):
    def __lt__(self, other):
        return self.data < other.data

from prioqueue import PrioQueue
class HuffmanPrioQ(PrioQueue):
    def number(self):
        return len(self._elems)

def HuffmanTree(weights):
    trees = HuffmanPrioQ()
    # O(mlogm)
    for w in weights:
        trees.enqueue(HTNode(w)) #重新定义了小于比较操作
    while trees.number() > 1:
        t1 = trees.dequeue()
        t2 = trees.dequeue()
        x = t1.data + t2.data
    # O(mlog(m))
        trees.enqueue(HTNode(x,t1,t2))
    # 空间复杂度O(2m-1) = O(m)
    return trees.dequeue()