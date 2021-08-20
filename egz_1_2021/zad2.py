from zad2testy import runtests
from collections import deque


def robot( L, A, B ):
    r = len(L)
    c = len(L[0])

    A = (A[1], A[0])
    B = (B[1], B[0])

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

    
runtests( robot )


