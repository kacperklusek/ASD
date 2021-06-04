def max_extending_pathG(G, s, t):
    def relax(u, v, cap):
        nonlocal cpcty, G, parent
        if cpcty[v] < min(cpcty[u], cap):
            cpcty[v] = min(cpcty[u], cap)
            parent[v] = u

    n = len(G)

    # cpcty[i] - największa możliwa pojemność ścieżki prowadzącej z s do i
    cpcty = [float("-inf") for _ in range(n)]
    cpcty[s] = float("inf")
    parent = [-1 for _ in range(n)]
    processed = [0 for _ in range(n)]
    n_of_processed = 0

    while n_of_processed < n:
        # wybieram wierzchołek o największym oszacowaniu O(V)
        u = -1
        for i in range(n):
            if not processed[i] and (u == -1 or cpcty[i] > cpcty[u]):
                u = i

        for neigh in G[u]:
            v, cap = neigh
            if not processed[v]:    # ewentualnie dodać:    and v != parent[u]
                relax(u, v, cap)

        processed[u] = 1
        n_of_processed += 1

    path = [t]
    while parent[t] != -1:
        t = parent[t]
        path.append(t)

    path.reverse()

    return path


G = [[(1, 4), (2, 3)],
     [(3, 2)],
     [(3, 5)],
     []]

print(max_extending_pathG(G, 0, 3))
