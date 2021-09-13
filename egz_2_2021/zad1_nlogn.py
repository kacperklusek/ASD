from zad1testy import runtests

def binsearch(tab, val):
    n = len(tab)
    l, r = 0, n-1
    while l <= r:
        idx = (l + r) // 2
        if tab[idx] < val:
            l = idx+1
        elif tab[idx] > val:
            r = idx-1
        else:
            return idx
    return False


def intuse(I, x, y):
    n = len(I)

    def DFS_visit(i, G, visited):
        visited[i] = 1
        for j in G[i]:
            if not visited[j]:
                DFS_visit(j, G, visited)

    T = []
    for l, r in I:
        T.append(l)
        T.append(r)
    T.sort()

    P = [T[0]]
    for i in range(1, 2*n):
        if T[i] != T[i-1]:
            P.append(T[i])

    n = len(P)

    if x not in P or y not in P:
        return []

    G1 = [[] for _ in range(n)]
    G2 = [[] for _ in range(n)]
    visited1 = [0] * n
    visited2 = [0] * n

    for l, r in I:
        v1 = binsearch(P, l)
        v2 = binsearch(P, r)
        G1[v1].append(v2)
        G2[v2].append(v1)

    DFS_visit(binsearch(P, x), G1, visited1)
    DFS_visit(binsearch(P, y), G2, visited2)

    output = []

    for i in range(len(I)):
        l, r = I[i]
        if visited1[binsearch(P, l)] and visited2[binsearch(P, r)]:
            output.append(i)

    return output



runtests(intuse)