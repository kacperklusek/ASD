def zbigniew(A):
    n = len(A)

    A = [min(A[i], n-1) for i in range(n)]

    # f[i][j] - minimalna liczba skoków potrzebna by dotrzeć do pola o numerze i, mając j energii
    f = [[float('inf') for _ in range(n)] for __ in range(n)]

    # na pozycje 0 potrzebuje 0 skoków
    f[0][A[0]] = 0

    for i in range(1, n):
        for j in range(n):
            for k in range(i):
                y = i - k + j - A[i]
                if n > y >= 0:
                    f[i][j] = min(f[i][j], f[k][y] + 1)

    return min(f[n-1])




# A = [2, 2, 0, 1, 0, 0]
A = [4, 5, 2, 4, 1, 2, 1, 0]

print(zbigniew(A))
