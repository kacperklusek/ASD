def DFS(G):  # reprezenacja macierzowa
    n = len(G)
    visited = 2
    V = [0 for i in range(n)]

    def DFS_visit(i):
        nonlocal visited, G, V
        V[i] = visited
        for j in range(n):
            if G[i][j] == 1 and V[j] != visited:
                print(f"visiting {j} from {i}") # zakomentować
                DFS_visit(j)

    DFS_visit(0)


g = [
    [0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

DFS(g)
