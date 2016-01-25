from collections import deque, defaultdict
 
def kahn_topsort(graph):
    in_degree = { u : 0 for u in graph }     # determine in-degree 
    for u in graph:                          # of each node
        for v in graph[u]:
            in_degree[v] += 1
 
    Q = deque()                 # collect nodes with zero in-degree
    for u in in_degree:
        if in_degree[u] == 0:
            Q.appendleft(u)
 
    L = []     # list for order of nodes
     
    while Q:                
        u = Q.pop()          # choose node of zero in-degree
        L.append(u)          # and 'remove' it from graph
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                Q.appendleft(v)
 
    if len(L) == len(graph):
        return L
    else:                    # if there is a cycle,  
        return []            # then return an empty list

# dependency_graph = {"spotlight_status_page": ["s3_viewer"], "rendang_viewer": [], "s3_viewer": []}

def invert(graph):
    new_graph = defaultdict(list)
    for task, dependencies in graph.items():
        for dep in dependencies:
            new_graph[dep].append(task)
        if task not in new_graph:
            new_graph[task] = []

    return dict(new_graph)

# print(kahn_topsort(invert(dependency_graph)))

def tasks_order(graph):
    return kahn_topsort(invert(graph))