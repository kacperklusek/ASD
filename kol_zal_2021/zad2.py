from zad2testy import runtests

# znajduje jakiwierzchołek należy usunąć, żeby graf rozpadł się na jak najwięcej rozłącznych kawałków

def breaking(G):
    n = len(G)

    # będę zapisywał stopnie wierzchołków
    degrees = [0 for _ in range(n)]
    parent = [None for _ in range(n)]
    visited = [0 for _ in range(n)]
    low = [float('inf') for _ in range(n)]
    d = [float('inf') for _ in range(n)]
    depth = 0

    def DFS_visit(i):
        nonlocal visited, G, degrees, d, depth, low, parent
        visited[i] = 1
        d[i] = depth
        depth += 1

        for j in range(n):
            if G[i][j] == 1 and not visited[j]:
                degrees[i] += 1
                degrees[j] += 1
                parent[j] = i

                DFS_visit(j)

        for k in range(n):
            low[i] = min(low[i], d[i])
            if G[i][k] and k != parent[i]:
                low[i] = min(low[i], low[k], d[k])


    root = 0

    DFS_visit(root)

    best = root if degrees[root] > 1 else None

    for i in range(n):
        if i != root and d[parent[i]] <= low[i] and parent[i] != root:
            if best is None or degrees[parent[i]] > degrees[best]:
                best = parent[i]

    return best


runtests( breaking )