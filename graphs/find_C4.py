def DFS(G, curr, parent, n, parents, vals):
    for neigh in range(n):
        if G[curr][neigh] == 1 and vals[neigh]:
            return True, neigh
        elif G[curr][neigh] == 1 and neigh != parent:
            vals[neigh] = 1
            parents[neigh] = curr

    return False, False


def restore(x, y, n):
    for i in range(n):
        x[i], y[i] = None, None


def find_c4(G):
    n = len(G)
    parents = [None for _ in range(n)]
    vals = [None for _ in range(n)]

    for i in range(n):
        for neigh in range(n):
            if G[i][neigh] == 1:
                bol, v = DFS(G, neigh, i, n, parents, vals)
                if bol:
                    print(f"({i}->{parents[v]}->{v}->{neigh})  CYKL")
                    return
        restore(parents, vals, n)


graph = [[0, 1, 0, 0, 0, 0, 0],
         [1, 0, 1, 1, 1, 0, 0],
         [0, 1, 0, 1, 0, 0, 1],
         [0, 1, 1, 0, 1, 0, 0],
         [0, 1, 0, 1, 0, 1, 0],
         [0, 0, 0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0, 0, 0]]
# graph = [[0, 1, 1, 1],
#          [1, 0, 1, 1],
#          [1, 1, 0, 1],
#          [1, 1, 1, 0]]


find_c4(graph)
