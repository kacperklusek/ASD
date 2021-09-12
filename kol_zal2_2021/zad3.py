from zad3testy import runtests


def paths(G,s,t):
    def relax1(u, v, w):
        nonlocal d1, parent1
        if d1[v] > d1[u] + w:
            d1[v] = d1[u] + w
            parent1[v] = u

    def relax2(u, v, w):
        nonlocal d2, parent2
        if d2[v] > d2[u] + w:
            d2[v] = d2[u] + w
            parent2[v] = u

    n = len(G)

    d1 = [float("inf") for _ in range(n)]
    d2 = [float("inf") for _ in range(n)]
    d1[s] = d2[t] = 0
    parent1 = [-1 for _ in range(n)]
    parent2 = [-1 for _ in range(n)]
    processed1 = [0 for _ in range(n)]
    processed2 = [0 for _ in range(n)]
    n_of_processed = 0

    while n_of_processed < n:
        u = -1
        for i in range(n):
            if not processed1[i] and (u == -1 or d1[i] < d1[u]):
                u = i

        for v, w in G[u]:
            if not processed1[v] and v != parent1[u]:
                relax1(u, v, w)

        processed1[u] = 1
        n_of_processed += 1

    n_of_processed = 0
    while n_of_processed < n:
        u = -1
        for i in range(n):
            if not processed2[i] and (u == -1 or d2[i] < d2[u]):
                u = i

        for v, w in G[u]:
            if not processed2[v] and v != parent2[u]:
                relax2(u, v, w)

        processed2[u] = 1
        n_of_processed += 1


    d = d1[t]
    if not d < float('inf'):
        return 0

    # odtwarzanie wyniku
    cnt = 0
    for i in range(n):
        for j, w in G[i]:
            if d1[i] + d2[i] == d1[j] + d2[j] == d and (d1[j] == d1[i] + w or d2[j] == d2[i] + w):
                cnt += 1

    cnt //= 2

    return cnt


    
runtests( paths )


