def LCS(A, B):
    n_a = len(A)
    n_b = len(B)
    F = [[None for _ in range(n_b)] for __ in range(n_a)]
    # F[i][j] = LCS of A[:i+1] and B[:j+1]

    for i in range(n_a):
        F[i][0] = 1 if A[i] == B[0] else 0
    for i in range(n_b):
        F[0][i] = 1 if A[0] == B[i] else 0

    for i in range(1, n_a):
        for j in range(1, n_b):
            F[i][j] = F[i-1][j-1] + 1 if A[i] == B[j] else max(F[i-1][j], F[i][j-1])

    return F[n_a-1][n_b-1]




A = ['A', 'G', 'G', 'T', 'A', 'B']
B = ['G', 'X', 'T', 'X', 'A', 'Y', 'B']

print(LCS(A, B))
