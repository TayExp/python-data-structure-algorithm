from dictBinTree import Assoc,BinTNode,DictBinTree
class AVLNode(BinTNode):
    def __init__(self,data):
        BinTNode.__init__(self.data)
        # bf域
        self.bf = 0

class DictAVL(DictBinTree):
    def __init__(self):
        """建立空树"""
        DictBinTree.__init__(self)


    @staticmethod
    def LL(a,b):
        a.left = b.right
        b.right = a
        b.bf = a.bf = 0
        return b

    @staticmethod
    def RR(a,b):
        a.right = b.left
        b.left = a
        b.bf = a.bf = 0
        return b

    @staticmethod
    def LR(a,b):
        c = b.right
        b.right, a.left = c.left, c.right
        c.left, c.right = b, a
        if c.bf == 0:
            b.bf = a.bf =0
        elif c.bf == 1:
            b.bf = 0
            a.bf = -1
        else:
            b.bf = 1
            a.bf = 0
        c.bf = 0
        return c

    @staticmethod
    def RL(a, b):
        c = b.left
        a.right, b.left = c.left, c.right
        c.left, c.right = a,b
        if c.bf == 0:
            b.bf = a.bf = 0
        elif c.bf == 1:
            a.bf = 0
            b.bf = -1
        else:
            a.bf = 1
            b.bf = 0
        c.bf = 0
        return c
    # 插入操作
    def insert(self, key, value):
        a = p =self._root
        if a is None:
            self._root = AVLNode(Assoc(key,value))
        # pa是a的父节点
        pa = q = None
        while p is not None:
            if key == p.data.key:
                p.data.value = value
                return
            if p.bf != 0: #已知最小非平衡子树
                pa, a = q, p #pa a记录最小非平衡子树
            q = p # q是p的父节点
            if key < q.data.key:
                p = p.left
            else:
                p = p.right
        # p is None,q是要插入点的父节点
        node = AVLNode(Assoc(key,value))
        if key < q.data.key:
            q.left = node
        else:
            q.right = node
        # L型还是R型
        if key<a.data.key:
            p = b = a.left
            d = 1
        else:
            p = b = a.right
            d = -1
        # 修改到新节点路径上的bf值
        while p != node:
            if key < p.data.key:
                p.bf = 1
                p = p.left
            else:
                p.bf = -1
                p = p.right
        # a bf 值为0或-d不会失衡
        if a.bf == 0:
            a.bf = d
            return
        if a.bf == -d:
            a.bf = 0
            return
        # 新节点在较高子树，失衡，局部调整
        if d == 1:
            if b.bf == 1:
                b = self.LL(a,b)
            else:
                b = self.LR(a,b)
        else:
            if b.bf == -1:
                b = self.RR(a,b)
            else:
                b = self.RL(a,b)
        if pa is None:
            self._root = b
        else:
            if pa.left == a:
                pa.left = b
            else:
                pa.right = b

    # 删除操作
    def delete(self,key):
        pass