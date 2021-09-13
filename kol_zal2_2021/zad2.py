from zad2testy import runtests


def order(L,K):
    n = len(L)
    M = 10**K

    beg = [[] for _ in range(M)]

    for i in range(n):
        num = L[i]
        beg[num // M].append(i)

    G = [[] for _ in range(n)]

    # lista sąsiedztwa
    for i in range(n):
        G[i] = beg[L[i] % M]

    # sortuje topologicznie
    visited = [0 for _ in range(n)]
    output = []

    def DFS_visit(i):
        nonlocal visited, G, output
        visited[i] = 1
        for j in G[i]:
            if not visited[j]:
                DFS_visit(j)

        output.append(i)

    for i in range(n):
        if not visited[i]:
            DFS_visit(i)

    output.reverse()
    output = [L[i] for i in output]

    return output




    
runtests( order )


