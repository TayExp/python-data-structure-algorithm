from Graph import Graph, inf
from SStack import Sstack
def DFS_graph_v0(graph, v0, visited):
    # 首先访问v0
    visited[v0] = 1
    DFS_seq = [v0]                      # DFS_seq记录遍历序列
    st = Sstack()
    # 入栈v0的所有邻接顶点，首先访问v0邻接顶点中的第一个
    st.push((0,graph.out_edges(v0)))    # 入栈(i,edges)
    while not st.is_empty():
        # 这次要访问edges[i]
        i, edges = st.pop() #pop#
        if i < len(edges): # 可以同时考虑到edges为空和访问完edges
            v, e = edges[i]
            # 回溯到i+1，访问edges[i+1]
            st.push((i+1, edges))    #push#
            # 寻找未被访问的顶点
            if not visited[v]:
                DFS_seq.append(v)
                visited[v] = 1
                # 深度优先搜索，每次访问v的第一个邻接顶点
                st.push((0, graph.out_edges(v))) #push#
    return DFS_seq

def DFS_graph(graph):
    vnum = graph.vertex_num()
    visited = [0] * vnum                # visited记录已访问节点
    DFS_seq = []
    for v0 in range(vnum):
        if visited[v0] == 0:
            seq = DFS_graph_v0(graph, v0, visited)
            DFS_seq.append(seq)
    return DFS_seq

g1 = Graph([[0,inf,7,inf],[4,0,inf,10],[inf,inf,0,2],[8,inf,1,0]])
g1.add_vertex([1,inf,6,inf],[9,2,3,inf])
print(g1)
for i in range(g1.vertex_num()):
    print(g1.out_edges(i))
print(DFS_graph(g1))