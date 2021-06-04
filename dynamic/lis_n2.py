from random import randint, seed

def LIS(A):
    n = len(A)
    F = [1 for _ in range(n)]

    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            if A[j] > A[i]:
                F[i] = max(F[i], F[j] + 1)

    print(F)
    return max(F)


seed(42)
n = 15
A = [randint(1, n*n) for _ in range(n)]
print(A)
print(LIS(A))