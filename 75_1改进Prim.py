from Graph import Graph,inf

class DecPrioHeap:
    """可减权堆"""
    def __init__(self,enlist,vnum):#(w,index,other)
        self._elems = list(enlist)
        self.vnum = vnum
        if self._elems:
            self.buildheap()
            self._weight = [None]*vnum
            for i in range(len(self._elems)):
                w,index,other = self._elems[i]
                # index是V-U集合中的点的序号，w是从U到index的最小权的边的权
                self._weight[index] = [w,i] #i 是index在_elems的位置序号

    def buildheap(self):
        end = len(self._elems)
        for i in range(end // 2, -1, -1):  # 从最右最下分支节点到堆顶逐一建堆
            self.siftdown(self._elems[i], i, end)

    def siftdown(self, e, begin, end):
        elems, i, j = self._elems, begin, begin * 2 + 1
        while j < end:
            if j + 1 < end and elems[j + 1] < elems[j]:
                j += 1
            # 三个数据，e最小，找到了合适的位置
            if e < elems[j]:
                break
            elems[i] = elems[j]  # elems[j]最小，上移
            i, j = j, j * 2 + 1
        elems[i] = e


    def siftup(self, e, last):
        i, j = last, (last - 1) // 2  # e和其父节点的索引
        while i > 0 and self._elems[j] > e:
            self._elems[i] = self._elems[j]
            i, j = j, (j - 1) // 2
        self._elems[i] = e

    def is_empty(self):
        return self._elems

    def weight(self,index):
        return self._weight[index][0]

    def dec_weight(self,index,w,other):
        # 更小，往上修改
        self._weight[index][0] = w
        last = self._weight[index][1]
        e = (w,index,other)
        self.siftup(e, last)

    def get_min(self):
        if self.is_empty():
            return None
        e0 = self._elems[0]
        e = self._elems.pop() # 从原堆最后取出一个元素，将这个元素放入堆顶
        if len(self._elems) > 0: #取出后不空
            self.siftdown(e, 0, len(self._elems))
        return e0


def Prim(graph):
    """对连通网络操作"""
    vnum = graph.vertex_num()
    wv_seq = [[graph.get_edge(0,v), v, 0] for v in range(vnum)] #(0,0,0)
    connects = DecPrioHeap(wv_seq,vnum)
    mst = [None] * vnum
    while not connects.is_empty():
        w, mv, u = connects.get_min()
        if w == inf:
            break
        mst[mv] = ((u,mv),w)
        for vi, m in graph.out_edges(mv):
            if not mst[vi]  and w < connects.weight(vi):
                connects.dec_weight(vi,w,mv) # vi=index在V-U中，更短就修改
    return mst