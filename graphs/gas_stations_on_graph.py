from queue import PriorityQueue

def refuel(G, D, C, s, t):
    n = len(G)

    processed = [[0 for _ in range(n)] for __ in range(D+1)]
    parent = [[-1 for _ in range(n)] for __ in range(D+1)]
    d = [[float('inf') for _ in range(n)] for __ in range(D+1)]

    def relax(u, v, j, k):
        nonlocal d, G, parent, Q, C
        if d[j][v] > d[k][u] + (j-(k-G[u][v]))*C[v]:
            d[j][v] = d[k][u] +(j-(k-G[u][v]))*C[v]
            parent[j][v] = u
            Q.put((d[j][v], j, v))

    for i in range(n):
        d[i][s] = i*C[s]
    Q = PriorityQueue()
    for i in range(D):
        Q.put((d[i][s], i, s))

    while not Q.empty():
        # wybieram wierzchołek o najmniejszym oszacowaniu
        du, k, u = Q.get()
        print('', end='')
        for v in range(n):
            if G[u][v] != -1:
                for j in range(0, k-G[u][v]+1):
                    if not processed[j][v] and v != parent[k][u]:
                        print('', end='')
                        relax(u, v, j, k)

        processed[k][u] = 1


    # print(d)  # tablica odległości
    return min([d[i][t] for i in range(n)])


G = [[-1, 4, 2, -1, -1],
     [-1, -1, -1, 5, 1],
     [-1, 1, -1, 1, -1],
     [-1, -1, -1, -1, -1],
     [-1, -1, -1, 2, -1]]
D = 5
C = [5, 1, 20, 1, 1]

print(refuel(G, D, C, 0, 3))
