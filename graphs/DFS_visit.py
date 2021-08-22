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



# z LOW - czyli do rozspójniania grafu (wikipedia punkty artykulacji)
# korzeń to 0

def DFS(G):  # reprezenacja macierzowa
    n = len(G)
    visited = [0 for _ in range(n)]
    parent = [None for _ in range(n)]
    low = [float('inf') for _ in range(n)]
    d = [0 for _ in range(n)]
    depth = 0

    def DFS_visit(i):
        nonlocal visited, G, visited, low, d, depth
        visited[i] = 1
        d[i] = depth
        depth += 1

        for j in range(n):
            if G[i][j] == 1 and not visited[j]:
                parent[j] = i
                DFS_visit(j)

        # wyznaczma wartość low[i] na powrocie
        for k in range(n):
            low[i] = min(low[i], d[i])
            if G[i][k] and k != parent[i]:
                low[i] = min(low[i], low[k], d[k])


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
