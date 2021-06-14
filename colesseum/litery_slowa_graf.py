from queue import PriorityQueue


def foo(G, W):
    L, E = G
    n = len(L)

    def relax(u, v, w, idx):
        nonlocal d, parent, Q
        if d[idx][v] > d[idx-1][u] + w:
            d[idx][v] = d[idx-1][u] + w
            parent[idx][v] = u
            Q.put((d[idx][v], idx, v))

    # lista sąsiedztwa
    edges = [[] for _ in range(n)]
    for u, v, w in E:
        edges[u].append([v, w])
        edges[v].append([u, w])

    # inicjalizacja tablic pomocniczych
    parent = [[-1 for _ in range(n)] for __ in range(len(W))]
    d = [[float('inf') for _ in range(n)] for __ in range(len(W))]
    for i in range(n):
        if L[i] == W[0]:
            d[0][i] = 0

    # inicjalizacja kolejki
    Q = PriorityQueue()
    for i in range(n):
        if L[i] == W[0]:
            Q.put((0, 0, i))

    # relaksacja krawędzi po kolei
    while not Q.empty():
        du, idx, u = Q.get()

        for v, w in edges[u]:
            if idx < len(W)-1 and L[v] == W[idx + 1]:
                relax(u, v, w, idx + 1)

    # odtwarzanie wyniku
    m = float('inf')
    idx = None
    pos = len(W) - 1
    for i in range(n):
        if L[i] == W[pos]:
            if d[pos][i] < m:
                m = d[pos][i]
                idx = i

    path = [idx]
    while parent[pos][idx] != -1:
        idx = parent[pos][idx]
        pos -= 1
        path.append(idx)
    path.reverse()

    return path, m


L = ['k', 'k', 'o', 'o', 't', 't']
E = [(0, 2, 2), (1, 2, 1), (1, 4, 3), (1, 3, 2), (2, 4, 5), (3, 4, 1), (3, 5, 3)]
G = (L, E)
W = 'kto'
W1 = 'kok'
W2 = 'kot'
W3 = 'kokot'

print(' - '.join(map(str, foo(G, W))))
print(' - '.join(map(str, foo(G, W1))))
print(' - '.join(map(str, foo(G, W2))))
print(' - '.join(map(str, foo(G, W3))))



