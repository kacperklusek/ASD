from collections import deque
from zad2testy import runtests


def BFS(G, s):
    n = len(G)
    queue = deque([s])

    d = [-1 for _ in range(n)]
    d[s] = 0

    def BFS_visit(i):
        nonlocal G, queue, d
        for j in G[i]:
            if d[j] < 0:
                d[j] = d[i] + 1  # d[i] == d[parent[j]]
                queue.appendleft(j)

    while len(queue) > 0:
        BFS_visit(queue.pop())

    return d


def enlarge(G, s, t):
    n = len(G)

    d1 = BFS(G, s)
    d2 = BFS(G, t)

    dist = d1[t]    # = d2[s]

    count_dist = [0 for _ in range(dist+1)]
    for i in range(n):
        if d1[i] + d2[i] == dist:
            count_dist[d1[i]] += 1

    goal = None
    for i in range(dist):
        if count_dist[i] == 1 == count_dist[i+1]:
            goal = i
            break

    if goal is None:
        return None

    for i in range(n):
        if d1[i] == goal:
            for j in G[i]:
                if d1[j] == d1[i] + 1 and d1[j]+d2[j] == dist:
                    return i, j





    pass


runtests( enlarge ) 
