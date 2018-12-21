class BinTNode(object):
    """二叉树结点"""
    def __init__(self, dat, left=None, right=None):
        self.data = dat
        self.left = left
        self.right = right

t = BinTNode(1, BinTNode(2,BinTNode(5)),BinTNode(3))

# 计算节点数
def count_BinTNodes(t):
    if t is None:
        return 0
    else:
        return 1 + count_BinTNodes(t.left) + count_BinTNodes(t.right)

# 计算所有数值和
def sum_BinTNodes(t):
    if t is None:
        return 0
    else:
        return t.data + sum_BinTNodes(t.left) + sum_BinTNodes(t.right)

# 递归定义的遍历算法
# def preorder(t,proc):
#     """先根遍历"""
#     # 断言语句
#     assert(isinstance(t,BinTNode))
#     if t is None:
#         return
#     proc(t.data)
#     preorder(t.left)
#     preorder(t.right)

# 带括号的前缀输出
def print_BinTNodes(t):
    if t is None:
        print("^",end="")
        return
    print("(" + str(t.data),end="")
    print_BinTNodes(t.left)
    print_BinTNodes(t.right)
    print(")",end="")

print_BinTNodes(t)
from SQueue import Squeue
# 宽度优先遍历
def levelorder(t,proc):
    qu = Squeue()
    qu.enqueue(t)
    while not qu.is_empty():
        t = qu.dequeue()
        if t is None:
            continue
        qu.enqueue(t.left)
        qu.enqueue(t.right)
        proc(t.data) #宽度优先，队列，先进先出

from SStack import *
# 非递归的先根序遍历
def preorder_nonrec(t, proc):
    s = Sstack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t.right) #右分支入栈
            proc(t.data)  # 先根序处理根数据
            t = t.left #先处理左分支
        t = s.pop() #遇到空树，回溯

preorder_nonrec(t, lambda x:print(x, end=" "))

# 迭代器
def preorder_elements(t):
    s = Sstack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t.right)
            yield t.data
            t = t.right
        t = s.pop()


# 非递归的后根序遍历
def postorder_nonrec(t,proc):
    s = Sstack()
    while t is not None or not s.is_empty():
        while t is not None: #下行循环直到栈顶的两子树空
            s.push(t) #根节点入栈
            t = t.left if t.left is not None else t.right #先左右子节点
        t = s.pop()  # 栈顶是应该访问的节点
        proc(t.data) # 操作
        if not s.is_empty() and s.peek().left == t:
            t = s.peek().right
        else:
            t = None