def transpose(G):
    adj_dict = {}
    for v in G.keys():
        adj_dict[v] = []
    for v in G.keys():
        for u in G[v]:
            adj_dict[u].append(v)
    return adj_dict


def dfs(graph, v, visited, stack):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, stack)
    stack.append(v)


def Kosaraju(G):
    stack = []
    visited = [False] * len(G.keys())
    # top sort in stack
    for i in range(len(G.keys())):
        if not visited[i]:
            dfs(G, i, visited, stack)

    transposed = transpose(G)
    visited = [False] * len(G.keys())
    strongly_connected_components = []

    while stack:
        v = stack.pop()
        if not visited[v]:
            component = []
            dfs(transposed, v, visited, component)
            strongly_connected_components.append(component)

    return strongly_connected_components