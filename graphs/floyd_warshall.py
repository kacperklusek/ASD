def floyd_warshall(G):
    n = len(G)

    d = [[1 if G[__][_] else 0 for _ in range(n)] for __ in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if not d[i][j]:
                    d[i][j] = d[i][k] and d[k][j]

    for i in range(n):
        print(d[i])


G = [[0, 0, 0, 0, 1, 1],
     [0, 0, 0, 1, 0, 1],
     [0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 1],
     [0, 0, 0, 0, 0, 0]]

floyd_warshall(G)
