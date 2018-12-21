# 大于任何float类型的值
inf = float("inf")
class GraphError(SyntaxError):
    pass
# 邻接矩阵实现图类
class Graph:
    def __init__(self, mat, unconn=inf, vi2vi=0):
        """
        :param mat: 初始的邻接矩阵对
        :param unconn: 无关联（边）情况的值，默认为inf
        :param vi2vi: 给出顶点到自身的默认值，默认为0
        """
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum: #检查是否为方阵
                raise ValueError("Argument for 'Graph'.")
        self._vnum = vnum
        self._out_edges = [0] * vnum #0表示没有计算过
        self._vi2vi = vi2vi
        self._unconn = unconn
        self._mat = [mat[i][:] for i in range(vnum)]

    def vertex_num(self):
        return self._vnum

    def _invalid(self,v):
        return 0 > v or v >= self._vnum

    def add_vertex(self,row,col):
        if len(row) != self._vnum or len(col) != self._vnum:  # 检查是否有n个元素
            raise ValueError("need list of old-vnum-weights")
        for i in range(self._vnum):
            self._mat[i].append(col[i])
        row1 = row[:]
        row1.append(self._vi2vi)
        self._mat.append(row1)
        self._vnum += 1
        self._out_edges.append(0)

    def add_edge(self,vi,vj,val=1):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + "or" + str(vj) +
                             "is not a valid vertex.")
        self._mat[vi][vj] = val

    def get_edge(self,vi,vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + "or" + str(vj) +
                             "is not a valid vertex.")
        return self._mat[vi][vj]

    def out_edges(self,vi):
        if self._invalid(vi):
            raise GraphError(str(vi) + "is not a valid vertex.")
        if self._out_edges[vi] == 0:
            self._out_edges[vi] = self._out_edges_method(self._mat[vi],self._unconn,vi)
        return self._out_edges[vi] # 可能重复计算没有邻接边的顶点

    @staticmethod
    def _out_edges_method(row,unconn,vi):
        edges = []
        for i in range(len(row)):
            if row[i] != unconn and i != vi:
                edges.append((i,row[i])) # 边的终点和边的信息
        return edges

    def __str__(self):
        return "[\n" +\
               ",\n".join(map(str,self._mat)) +\
               "\n]" + "\nUnconnected:" + str(self._unconn)

class GraphAL(Graph):
    def __init__(self, mat, unconn=inf, vi2vi=0):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum: #检查是否为方阵
                raise ValueError("Argument for 'GraphAL'.")
        self._vnum = vnum
        self._vi2vi = vi2vi
        self._unconn = unconn
        self._mat = [Graph._out_edges_method(mat[i],unconn,i)
                     for i in range(vnum)]

    def add_vertex(self,row,col):
        self._mat.append([])
        vnum = self._vnum
        self._vnum += 1
        for i in range(vnum):
            if col[i] < inf:
                self.add_edge(i,vnum,col[i])
            if row[i] < inf:
                self._mat[vnum].append((i,row[i]))
        return self._vnum - 1

    def add_edge(self,vi,vj,val=1):
        if self._vnum == 0:
            raise GraphError("Cannot add edge to empty graph")
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + " or " + str(vj) +
                             "is not a valid vertex.")
        row = self._mat[vi]
        i = 0
        while i < len(row):
            if row[i][0] == vj:
                self._mat[vi][i] = (vj,val)
                return
            if row[i][0] > vj:
                break
            i += 1
        self._mat[vi].insert(i,(vj,val))

    def get_edge(self,vi,vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + "or" + str(vj) +
                             "is not a valid vertex.")
        for i, val in self._mat[vi]:
            if i == vj:
                return val
        return self._unconn

    def out_edges(self,vi):
        if self._invalid(vi):
            raise GraphError(str(vi) + "is not a valid vertex.")
        return self._mat[vi]


g1 = Graph([[0,4,6,7],[4,0,3,10],[inf,inf,0,2],[8,inf,1,0]])
print(g1)
print(g1.out_edges(2))
g1.add_edge(3,1,4)
print(g1.get_edge(3,1))
g1.add_vertex([3,inf,6,9],[9,2,3,inf])
print(g1.vertex_num())
print(g1)
print("-"*40)
g1 = GraphAL([[0,4,6,7],[4,0,3,10],[inf,inf,0,2],[8,inf,1,0]])
print(g1)
print(g1.out_edges(2))
g1.add_edge(3,1,4)
print(g1.get_edge(3,1))
g1.add_vertex([3,inf,6,9],[9,2,3,inf])
print(g1.vertex_num())
print(g1)