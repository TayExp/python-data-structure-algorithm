from SStack import Sstack
class BinTNode:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
# END class

class Assoc:
    def __init__(self,key,value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        return self.key < other.key

    def __le__(self, other):
        return self.key < other.key or self.key == other.key

    def __str__(self):
        return "Asso({0},{1})".format(self.key,self.value)
# END class

class DictBinTree:
    """基于排序二叉树的字典类"""
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def search(self,key):
        bt = self._root
        while bt is not None:
            entry = bt.data
            if key < entry.key:
                bt = bt.left
            elif key > entry.key:
                bt = bt.right
            else:
                return entry.value
        return None

    def insert(self,key,value):
        if self.is_empty():
            self._root = BinTNode(Assoc(key,value))
            return
        bt = self._root
        while True:
            entry = bt.data
            if key < entry.key:
                if bt.left is None:
                    bt.left = BinTNode(Assoc(key,value))
                    return
                bt = bt.left
            elif key > entry.key:
                if bt.right is None:
                    bt.right = BinTNode(Assoc(key,value))
                    return
                bt = bt.right
            else:
                bt.data.value = value
                return

    def values(self):
        """中序遍历"""
        t, s = self._root, Sstack()
        while t is not None or not s.is_empty():
            while t is not None:
                s.push(t)
                t = t.left
            t = s.pop()
            yield t.data.value
            t = t.right

    def entries(self):
        """中序遍历"""
        t, s = self._root, Sstack()
        while t is not None or not s.is_empty():
            while t is not None:
                s.push(t)
                t = t.left
            t = s.pop()
            yield t.data.key,t.data.value
            t = t.right

    def delete(self,key):
        """删除节点，局部调整"""
        # 维持p为q的父节点, 节点q从根节点开始
        p, q = None, self._root
        while q is not None and q.data.key != key:
            p = q
            if key < q.data.key:
                q = p.left
            else:
                q = p.right
        if q is None:
                return
        # 找到了节点q是要删除的节点
        if q.left is None:
            if p is None:
                self._root = q.right
            if q is p.left:
                p.left = q.right
            else:
                p.right = q.right
            return
        # q有左子树
        r = q.left
        # 左子树的最右节点
        while r.right is not None:
            r = r.right
        if p is None:
            self._root = q.left
        elif p.left is q:
            p.left = q.left
        else:
            p.right = q.left
        r.right = q.right

    def print(self):
        for k, v in self.entries():
            print(k,v)
# END class

def build_dictBinTree(entries):
    dic = DictBinTree()
    for k, v in entries:
        dic.insert(k, v)
    return dic

dic = DictBinTree()
dic.insert(1,"a")
dic.insert(2,"b")
dic.insert(3,"c")
dic.insert(4,"d")
dic.insert(6,"f")
dic.print()
for v in dic.values():
    print(v)
dic.delete(3)
dic.print()

# p, q = None, self._root # 维持p为q的父节点, 节点q从根节点开始
# while q is not None and q.data != key:
#     p = q
#     # 1确定删除节点
#     if key < q.data.key:
#         q = q.left
#     else:
#         q = q.right
# if q is None: # 没有该关键码的项
#     return
# # q不空，即为要删除的节点
# if q.left is None: #q没有左子节点
#     # 2 q是根节点
#     if p is None:
#         self._root = q.right
#     elif q is p.left:
#         p.left = q.right
#     else:
#         p.right = q.right
#     return
# # 3 q为删除的节点，且q有左子树
# r = q.left
# # 左子树的最右节点
# while r.right is not None:
#     r = r.right
# r.right = q.right
# p.left = q.left