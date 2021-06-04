from collections import deque





def BFS(G, start=0):  # repr macierzowa

    n = len(G)
    queue = deque([start])
    parent = [None for _ in range(n)]  # w sumie parent nie potrzebne
    visited = [False for _ in range(n)]
    visited[start] = True
    d = [-1 for _ in range(n)]
    d[start] = 0

    def BFS_visit(i):
        nonlocal G, queue, parent, visited, d
        for j in range(n):
            if G[i][j] == 1 and not visited[j]:
                parent[j] = i
                d[j] = d[i] + 1  # d[i] == d[parent[j]]
                queue.appendleft(j)
                visited[j] = True

    while len(queue) > 0:
        BFS_visit(queue.pop())

    BFS_visit(start)

    print(d)


# g = [[0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
#      [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#      [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#      [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0],
#      [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
#      [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0],
#      [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
#      [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], ]

g = [[0, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 1, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 1, 0],
     [0, 0, 0, 1, 1, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0]]

BFS(g)
