G = [[1, 6],
     [0, 2],
     [1, 6, 3],
     [2, 4, 5],
     [3, 5],
     [3, 4],
     [0, 2, 7],
     [6],
     ]

n = len(G)
G_matrix = [[0 for _ in range(n)] for __ in range(n)]
for i in range(n):
    for ind in G[i]:
        G_matrix[i][ind] = 1
        # G_matrix[ind][i] = 0


for i in range(n):
    print(G_matrix[i], ',')

