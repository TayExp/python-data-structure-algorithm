from Graph import Graph,inf
def critical_paths(graph):
    def events_earliest_time(vnum, graph, toposeq):
        ee = [0] * vnum
        # 从前往后更新
        for i in toposeq:
            for j, w in graph.out_edges(i):
                if ee[i] + w > ee[j]:
                    # 事件j应该更晚结束,要等i-->j上的活动做完才行
                    ee[j] = ee[i] + w
        return ee

    def event_latest_time(vnum, graph, toposeq, eelast):
        le = [eelast] * vnum
        for k in range(vnum-2,-1,-1):#逆拓扑顺序
            # end事件的最迟发生时间是确定的，从end-1=vnum-2开始
            i = toposeq[k]
            for j, w in graph.out_edges(i):
                if le[j] - w < le[i]:
                    # 事件i必须更早开始, 最迟也得是le[j]-w的时候
                    le[i] = le[j] - w
        return le

    def crt_path(vnum, graph, ee, le):
        crt_actions = []
        for i in range(vnum):
            for j, w in graph.out_edges(i):
                if ee[i] == le[j] - w:
                    crt_actions.append((i,j,ee[i]))
        return crt_actions

    toposeq = toposort(graph)
    if not toposeq:
        return False
    vnum = graph.vertex_num()
    ee = events_earliest_time(vnum,graph,toposeq)
    le = event_latest_time(vnum,graph,toposeq,ee)
    return crt_path(vnum,graph,ee,le)

def toposort(graph):
    vnum = graph.vertex_num()
    indegree, toposeq = [0]*vnum, []
    zerov = -1
    for vi in range(vnum):
        for v,w in graph.out_edges(vi):
            indegree[v] += 1
        if indegree[vi] == 0: # 初始0度表
            indegree[vi] = zerov
            zerov = vi
    for n in range(vnum):
        if zerov == -1:
            return False
        vi = zerov
        zerov = indegree[zerov]
        toposeq.append(vi)
        for v, w in graph.out_edges(vi):
            indegree[v] -= 1
            if indegree[v] == 0:
                indegree[v] = zerov
                zerov = v
    return toposeq