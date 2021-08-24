# MST

def kruskal(G):
    n = len(G)
    STree = []

    def find(v):
        nonlocal parent, rank
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(u, v):
        nonlocal parent, rank
        x, y = find(u), find(v)
        if rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[x] = y
            if rank[x] == rank[y]:
                rank[y] += 1

    E = []
    for u in range(n):
        for v in range(n):
            if G[u][v] != -1:
                E.append((G[u][v], u, v))
    E.sort()


    parent = [_ for _ in range(n)]
    rank = [1 for _ in range(n)]

    for w, u, v in E:
        if find(u) != find(v):
            STree.append([u, v])
            union(u, v)

    return STree


