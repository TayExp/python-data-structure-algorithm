from Graph import Graph,inf
def all_shorest_paths(graph):
    """Floyd算法求所有顶点最短路径，0，inf"""
    vnum = graph.vertex_num()
    a = [[graph.get_edge(i,j) for j in range(vnum)] for i in range(vnum)]
    for i in range(vnum):
        a[i][i] = 0
    nextvertex = [[-1 if a[i][j] == inf else j for j in range(vnum)]
                  for i in range(vnum)]
    for k in range(vnum):
        for i in range(vnum):
            for j in range(vnum):
                if a[i][j] > a[i][k] + a[k][j]:
                    a[i][j] = a[i][k] + a[k][j]
                    nextvertex[i][j] = nextvertex[i][k]
    return (a, nextvertex)