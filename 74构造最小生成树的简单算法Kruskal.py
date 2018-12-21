# 最小生成树：mst
# 代表元：reps[i]
from Graph import Graph
def Kruskal(graph):
    """对连通网络操作"""
    vnum = graph.vertex_num()
    reps = [i for i in range(vnum)]
    mst, edges = [], []
    for vi in range(vnum):
        for v,w in graph.out_edges(vi):
            edges.append((w,vi,v))
        edges.sort() # 按元组的大小排序
        for w, vi, vj in edges:
            if reps[vi] != reps[vj]:
                mst.append(((vi,vj),w))
                if len(mst) == vnum-1:
                    break
                # 合并连通变量，统一为vi的代表元
                rep, orep = reps[vi], reps[vj]
                for i in range(vnum):
                    if reps[i] == orep:
                        reps[i] = rep
    return mst
