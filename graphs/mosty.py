# algorytm:
# 1) wykonujemy DFS zapisując czasy odwiedzenia
# 2) obliczamy dla każdego wierzchołka funkcję low
#    low[v] = min ( czas odwiedzenia v, low[sąsiedzi ale nie rodzic v], low[dziecko v] )
# 3) mosty to krawędzie (v, parent[v]), gdzie d[v] = low[v]

def mosty(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    low = [None for _ in range(n)]
    d = [0 for _ in range(n)]
    low[0] = 0
    depth = 0

    def DFS_visit(i):
        nonlocal visited, G, parent, low, depth
        visited[i] = True
        depth += 1

        for j in range(n):
            if G[i][j] == 1 and not visited[j]:
                parent[j] = i
                d[j] = low[j] = depth
                DFS_visit(j)
                low[i] = min(low[i], low[j])
            elif G[i][j] == 1 and visited[j] and parent[i] != j:    # krawędź wsteczna
                low[i] = min(low[i], low[j])

    DFS_visit(0)    # 0 to punkt startowy

    for i in range(n):
        if d[i] == low[i] and parent[i] != -1:
            print(f'most: {parent[i]}-{i}')




g = [[0, 1, 0, 0, 0, 0, 1],
     [1, 0, 1, 0, 0, 1, 1],
     [0, 1, 0, 1, 1, 0, 0],
     [0, 0, 1, 0, 1, 0, 0],
     [0, 0, 1, 1, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 1],
     [1, 1, 0, 0, 0, 1, 0],
     ]

mosty(g)
