def bipartite(graph):
    n = len(graph.keys())
    colors = [-1] * n

    for start in range(n):
        if colors[start] == -1:
            queue = [start]
            colors[start] = 0

            while queue:
                u = queue.pop(0)
                for v in graph[u]:
                    if colors[v] == -1:
                        colors[v] = 1 - colors[u]
                        queue.append(v)
                    # Если сосед уже окрашен в тот же цвет, граф не двудольный
                    elif colors[v] == colors[u]:
                        return False, []

    set1 = [i for i in range(n) if colors[i] == 0]
    set2 = [i for i in range(n) if colors[i] == 1]

    return set1, set2
G = {}
G[0] = [1]
G[1] = [2,0]
G[2] = [3,1]
G[3]=[2]
L=bipartite(G)[0]
R=bipartite(G)[1]
def kuhn(graph, L, R):
    match = {u: -1 for u in R}
    visited = set()

    def dfs(v):
        for u in graph[v]:
            if u not in visited:
                visited.add(u)
                if match[u] == -1 or dfs(match[u]):
                    match[u] = v
                    return True
        return False

    max_matching = 0
    for v in L:
        visited = set()
        if dfs(v):
            max_matching += 1

    return max_matching, match
print(kuhn(G,L,R))
def search_min_ver_pok(graph):
    _, match = kuhn(graph, L, R)

    cover = set()
    for u in R:
        if match[u] != -1:
            if match[u] not in cover:
                cover.add(match[u])
            else:
                cover.add(u)

    return cover

print(search_min_ver_pok(G))