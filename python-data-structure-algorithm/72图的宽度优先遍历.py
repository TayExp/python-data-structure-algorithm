from Graph import Graph, inf
from SQueue import Squeue
def BFS_graph_v0(graph, v0, visited):
    # 首先访问v0
    visited[v0] = 1
    BFS_seq = [v0]                      # BFS_seq记录遍历序列
    sq = Squeue()
    sq.enqueue(v0)
    while not sq.is_empty():
        v = sq.dequeue()            #dequeue
        for u,w in graph.out_edges(v):
            if visited[u] == 0:
                sq.enqueue(u)        #enqueue
                BFS_seq.append(u)
                visited[u] = 1
    return BFS_seq

def BFS_graph(graph):
    vnum = graph.vertex_num()
    visited = [0] * vnum                # visited记录已访问节点
    BFS_seq = []
    for v0 in range(vnum):
        if visited[v0] == 0:
            seq = BFS_graph_v0(graph, v0, visited)
            BFS_seq.append(seq)
    return BFS_seq


g1 = Graph([[0,inf,7,inf],[4,0,inf,10],[inf,inf,0,2],[8,inf,1,0]])
g1.add_vertex([1,inf,6,inf],[9,2,3,inf])
print(g1)
for i in range(g1.vertex_num()):
    print(g1.out_edges(i))
print(BFS_graph(g1))