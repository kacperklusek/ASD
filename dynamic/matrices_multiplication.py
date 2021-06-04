# A = [[10, 100], [100, 10], [10, 1000], [1000, 10]]
A = [[10, 100], [100, 10], [10, 1000]]


#                 i             j
#                 k
#                   X           Y

def cost(A, B):
    return A[0] * A[1] * B[1]


def matrices(A):
    n = len(A)
    F = [[0 for _ in range(n)] for __ in range(n)]

    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            for k in range(i, j):
                X = [A[i][0], A[k][1]]
                Y = [A[k + 1][0], A[j][1]]
                if F[i][j] == 0:
                    F[i][j] = cost(X, Y) + F[i][k] + F[k + 1][j]
                else:
                    F[i][j] = min(F[i][j], cost(X, Y) + F[i][k] + F[k + 1][j])

    # print(F)
    return F[0][n - 1]


print(matrices(A))
