def DFS(G):  # reprezenacja macierzowa
    n = len(G)
    visited = [0 for _ in range(n)]

    def DFS_visit(i):
        nonlocal visited, G
        visited[i] = 1
        for j in range(n):
            if G[i][j] == 1 and not visited[j]:
                # print(f"visiting {j} from {i}") # zakomentować
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
