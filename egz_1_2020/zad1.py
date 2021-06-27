from zad1testy import runtests

# Złożoność programu to O(V²)

def islands(G, A, B):
    def relax(u, v):
        nonlocal d, graph, parent
        if d[v] > d[u] + graph[u][v]:
            d[v] = d[u] + graph[u][v]
            parent[v] = u

    def idx(a, b):
        return 3 * a + b

    n = len(G)

    # tworzę nowy graf przez rozmnażanie wierzchołków
    graph = [[0 for _ in range(3 * n)] for __ in range(3 * n)]
    for i in range(n):
        for j in range(n):
            mean = G[i][j]
            if mean == 1:
                graph[idx(i, 0)][idx(j, 1)] = graph[idx(i, 0)][idx(j, 2)] = 1
                graph[idx(i, 1)][idx(j, 0)] = graph[idx(i, 2)][idx(j, 0)] = 1
            elif mean == 5:
                graph[idx(i, 1)][idx(j, 0)] = graph[idx(i, 1)][idx(j, 2)] = 5
                graph[idx(i, 0)][idx(j, 1)] = graph[idx(i, 2)][idx(j, 1)] = 5
            elif mean == 8:
                graph[idx(i, 2)][idx(j, 0)] = graph[idx(i, 2)][idx(j, 1)] = 8
                graph[idx(i, 0)][idx(j, 2)] = graph[idx(i, 1)][idx(j, 2)] = 8

    d = [float("inf") for _ in range(3*n)]
    d[idx(A, 0)] = d[idx(A, 1)] = d[idx(A, 2)] = 0
    parent = [-1 for _ in range(3*n)]
    processed = [0 for _ in range(3*n)]
    n_of_processed = 0

    while n_of_processed < 3 * n:
        # wybieram wierzchołek o najmniejszym oszacowaniu O(V)
        u = -1
        for i in range(3*n):
            if not processed[i] and (u == -1 or d[i] < d[u]):
                u = i

        # relaksacja
        for v in range(3*n):
            if not processed[v] and graph[u][v] != 0 and v != parent[u]:
                relax(u, v)

        processed[u] = 1
        n_of_processed += 1

    return min(d[idx(B, 0)], d[idx(B, 1)], d[idx(B, 2)])


runtests(islands)

G = [0, 0, 0, 0, ]
