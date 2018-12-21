from Graph import Graph
from prioqueue import PrioQueue
def dijkstra_shortest_paths(graph, v0):
    vnum = graph.vertex_num()
    assert 0 <= v0 < vnum
    paths = [None] * vnum
    count = 0
    cands = PrioQueue([(0,v0,v0)])
    while count < vnum and not cands.is_empty():
        plen, u, vmin = cands.dequeue()
        if paths[vmin]:
            continue
        paths[vmin] = (u,plen)   #记录新确定的最短路径
        for v, w in graph.out_edges(vmin): #考察via新U顶点vmin的路径
            if not paths[v]: #v尚未知最短路径
                cands.enqueue((plen+w,vmin,v)) #新的路径加入候选，
        count += 1                  # 比较过程已经包含在入优先队列过程中了
    return paths