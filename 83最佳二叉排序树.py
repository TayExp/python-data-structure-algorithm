from  dictBinTree import DictBinTree,BinTNode,Assoc
class DicOptBinTree(DictBinTree):
    def __init__(self,seq):
        DictBinTree.__init__(self)
        data = sorted(seq)
        self._root = DictBinTree.buildOBT(data,0,len(data)-1)

    @staticmethod
    def buildOBT(data, start, end):
        if start>end:
            return None
        mid = (start+end)//2
        left = DicOptBinTree.buildOBT(data,start,mid-1)
        right = DicOptBinTree.buildOBT(data,mid+1,end)
        return BinTNode(Assoc(*(data[mid]),left,right))

dic = DictBinTree()
dic.insert(1,"a")
dic.insert(2,"b")
dic.insert(3,"c")
dic.insert(4,"d")
dic.insert(6,"f")
for i in dic.entries():
    print(i)
for v in dic.values():
    print(v)
dic.delete(3)
for i in dic.entries():
    print(i)

def build_opt_tree(wp,wq):
    """wp:internal nodes n
       wq:external nodes n+1"""
    num = len(wp) + 1
    if len(wq) != num:
        raise ValueError("Auruments of build_opt_btree are wrong.")
    # num*num， 分段权值， Tij的代价，root ij最佳根节点
    w = [[0]*num for j in range(num)]
    c = [[0]*num for j in range(num)]
    r = [[0]*num for j in range(num)]
    for i in range(num):
        # 上三角即可
        w[i][i] = wq[i]
        for j in range(i+1, num):
            w[i][j] = w[i][j-1] + wp[j-1] + wq[j]
    # 初始
    for i in range(num):
        c[i][i+1] = w[i][i+1]
        r[i][i+1] = i

    for m in range(2, num):
        for i in range(0,num - m):
            k0 , j = i, i+m
            wmin = float("inf")
            for k in range(i, j ):
                if c[i][k] + c[k+1][j] < wmin:
                    wmin = c[i][k] + c[k+1][j]
                    k0 = k
            c[i][j] = wmin
            r[i][j] = k
    return c,r