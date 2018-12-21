class Node(object):
    """二叉树结点"""
    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None

class BinTree(object):
    """二叉树"""
    def __init__(self):
        self.root = None

    def add(self,item):
        """增加一个节点"""
        node = Node(item)
        if self.root == None:
            self.root = node
            return
        queue = [self.root] #树结点的队列（列表）,open表
        while queue: # 如果不为空树，[None]也非空
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)



