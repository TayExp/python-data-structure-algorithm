from Graph import Graph, inf
from SQueue import Squeue

def DFS_span_forest(graph):
    vnum = graph.vertex_num()
    span_forest = [None] * vnum # None代表未访问过

    #递归遍历函数
    def dfs(graph, v):
        # 可以在外层函数使用，必须绑定一个外层的局部变量
        nonlocal span_forest
        for u, w in graph.out_edges(v):
            # 出口是v的所有邻接顶点都访问过
            if span_forest[u] is None:
                # span_forest[u] = (v,w)
                span_forest[u] = v
                dfs(graph,u)

    for v in range(vnum):
        if span_forest[v] is None:
            # span_forest[v] = (v,0)
            span_forest[v] = v
            dfs(graph,v)
    return span_forest


def BFS_span_forest(graph):
    vnum = graph.vertex_num()
    span_forest = [None] * vnum # None代表未访问过
    for v in range(vnum):
        if span_forest[v] is None:
            # span_forest[v] = (v,0)
            span_forest[v] = v
            sq = Squeue()
            sq.enqueue(v)
            while not sq.is_empty():
                v = sq.dequeue()
                for u, w in graph.out_edges(v):
                    if span_forest[u] is None:
                        # span_forest[u] = (v,w)
                        span_forest[u] = v
                        sq.enqueue(u)
    return span_forest

num = 7
g1 = Graph([[inf]*7]*7)
g1.add_edge(1,0,11)
g1.add_edge(0,2,6)
g1.add_edge(1,2,4)
g1.add_edge(2,1,3)
g1.add_edge(0,3,3)
g1.add_edge(3,4,5)
g1.add_edge(2,4,5)
g1.add_edge(4,6,9)
g1.add_edge(5,6,10)
g1.add_edge(1,5,7)
for i in range(g1.vertex_num()):
    print(g1.out_edges(i))
print("-"*30)
print(DFS_span_forest(g1))
print("-"*30)
print(BFS_span_forest(g1))