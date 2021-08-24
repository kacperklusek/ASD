from zad2testy import runtests
from math import sqrt, ceil

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

    # zmiennej can_be używam, żeby sprawdzić czy da się w ogole zrobić drzewo rozpinające

    E = []
    for u in range(n):
        can_be = False
        for v in range(n):
            if G[u][v] != 0:
                can_be = True
                E.append((G[u][v], u, v))
        if not can_be:
            return None

    E.sort()

    parent = [_ for _ in range(n)]
    rank = [1 for _ in range(n)]

    for w, u, v in E:
        if find(u) != find(v):
            STree.append([u, v])
            union(u, v)

    base = find(STree[0][0])
    for u, v in STree:
        if find(u) != base or find(v) != base:
            return None

    return STree


def get_diff(stree, G):
    n = len(G)
    mi = float('inf')
    ma = float('-inf')
    for u, v in stree:
       mi = ceil(G[u][v]) if ceil(G[u][v]) < mi else mi
       ma = ceil(G[u][v]) if ceil(G[u][v]) > ma else ma
    return ma-mi


def highway(A):
    n = len(A)

    G = [[sqrt((A[i][0] - A[j][0])**2 + (A[i][1] - A[j][1])**2) for i in range(n)] for j in range(n)]

    diff = float('inf')

    while 1:
        stree = kruskal(G)

        # jeśli nie da sie juz zrobic MST
        if stree is None:
            break

        diff = min(diff, get_diff(stree, G))
        u, v = stree[0]
        G[u][v] = G[v][u] = 0

    return diff




runtests( highway ) 
