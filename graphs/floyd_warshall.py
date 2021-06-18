# odleŋłości wszystkie-wszystkie

def floyd_warshall(G):
    n = len(G)

    d = [[G[i][j] if G[i][j] > 0 else float('inf') for i in range(n)] for j in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    return d
    # for i in range(n):
    #     print(d[i])


G = [[0, 0, 0, 0, 1, 1],
     [0, 0, 0, 1, 0, 1],
     [0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 1],
     [0, 0, 0, 0, 0, 0]]

floyd_warshall(G)
