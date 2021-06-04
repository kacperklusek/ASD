# V²

def dijkstra(G):
    def relax(u, v):
        nonlocal d, G, parent
        if d[v] > d[u] + G[u][v]:
            d[v] = d[u] + G[u][v]
            parent[v] = u

    n = len(G)

    s = 0   # wierzchołek startowy

    d = [float("inf") for _ in range(n)]
    d[s] = 0
    parent = [-1 for _ in range(n)]
    processed = [0 for _ in range(n)]
    n_of_processed = 0

    while n_of_processed < n:
        # wybieram wierzchołek o najmniejszym oszacowaniu O(V)
        u = -1
        for i in range(n):
            if not processed[i] and (u == -1 or d[i] < d[u]):
                u = i

        for v in range(n):
            if not processed[v] and G[u][v] != -1 and v != parent[u]:
                relax(u, v)

        processed[u] = 1
        n_of_processed += 1

    print(d)    # tablica odległości


graph = [[-1, 4, -1, -1, -1, -1, -1, 8, -1],
         [4, -1, 8, -1, -1, -1, -1, 11, -1],
         [-1, 8, -1, 7, -1, 4, -1, -1, 2],
         [-1, -1, 7, -1, 9, 14, -1, -1, -1],
         [-1, -1, -1, 9, -1, 10, -1, -1, -1],
         [-1, -1, 4, 14, 10, -1, 2, -1, -1],
         [-1, -1, -1, -1, -1, 2, -1, 1, 6],
         [8, 11, -1, -1, -1, -1, 1, -1, 7],
         [-1, -1, 2, -1, -1, -1, 6, 7, -1]]

dijkstra(graph)

