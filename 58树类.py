# 树的list实现
class SubtreeIndexError(ValueError):
    pass

def Tree(data, *subtrees):
    # 第一个成员表示节点，第二个成员表示子树序列
    t = [data]
    t.extend(subtrees)
    return t

def is_empty_tree(tree):
    return tree is None

def root(tree):
    return tree[0]

def subtree(tree,i):
    if i < 1 or i >= len(tree):
        raise SubtreeIndexError
    return tree[i]

def set_root(tree,data):
    tree[0] = data

def set_subtree(tree, i, subtree):
    if i < 1 or i >len(tree):
        raise SubtreeIndexError
    tree[i] = subtree


t1 = Tree('+',5,6,8)
print(t1)
print(subtree(t1,3))
print(t1)
t2 = Tree(root(t1),subtree(t1,3))
set_subtree(t1,2,t2)
print(t1)