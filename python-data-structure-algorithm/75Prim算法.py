from Graph import Graph
from prioqueue import PrioQueue
def Prim(graph):
    """对连通网络操作"""
    vnum = graph.vertex_num()
    mst = [None] * vnum
    cands = PrioQueue([(0,0,0)]) #记录候选边（w,vi,vj）
    count = 0
    while count < vnum and not cands.is_empty():
        w, u, v = cands.dequeue()
        if mst[v]: #邻接顶点已经在mst，即u v 在同一个集合，跳过继续
            continue
        mst[v] = ((u,v),w)
        count += 1
        for vi, m in graph.out_edges(v):
            if not mst[vi]:
                cands.enqueue((w,v,vi))
    return mst