
def zbigniew(A):
    n = len(A)
    maxenergy = A[0]

    for i in range(1, n):
        maxenergy += max(A[i] - 1, 0)

    F = [[None for _ in range(maxenergy + 1)] for __ in range(n)]

    F[0][A[0]] = 0
    for i in range(1, A[0]+1):
        F[i][A[0] - i + A[i]] = 1

    for i in range(n):
        for e in range(maxenergy + 1):
            if F[i][e] is not None:
                for k in range(1, e+1):
                    if F[i + k][e - k + A[i+k]] is None:
                        F[i + k][e - k + A[i + k]] = F[i][e] + 1
                    else:
                        F[i + k][e - k + A[i + k]] = min(F[i][e] + 1, F[i + k][e - k + A[i + k]])

    m = n
    for i in range(maxenergy+1):
        if F[n-1][i] is not None:
            m = min(m, F[n-1][i])

    return m



A = [2, 2, 1, 0, 0, 0]

print(zbigniew(A))
