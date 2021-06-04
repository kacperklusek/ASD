def tasks(T):
    n = len(T)
    visited = -1
    V = [0 for _ in range(n)]
    output = []

    def DFS_visit(i):
        nonlocal visited, T, V, output
        V[i] = visited
        for j in range(n):
            if T[i][j] == 1 and V[j] != visited:
                # print(f"visiting {j} from {i}")  # zakomentować
                DFS_visit(j)

        output.append(i)

    DFS_visit(0)

    output.reverse()
    return output


g = [[0, 1, 1, 0, 0, 0, 0, 1],
     [0, 0, 1, 0, 1, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 1, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0], ]

print(tasks(g))
