

def bin_search(num, N, n):
    i = n // 2
    l, r = 0, n - 1
    while 1:
        if N[i] < num <= N[i + 1]:
            return i + 1
        elif N[i] < num:
            l = i
        else:
            r = i
        i = (l + r) // 2


def printLIS(A, F, i, start):
    n = len(A)
    for r in range(start, -1, -1):
        if F[r] == i:
            printLIS(A, F, i-1, r)
            print(A[r])

def printAllLIS(A):
    n = len(A)
    m = max(A)  # O(n)
    F = [0] * n  # O(n) - funkcja
    N = [m+1] * (n + 1)  # O(n) - najlepsze końcówki ciągów
    N[0] = 0  # zakładając że liczby w A są > 0
    # P = [[] for _ in range(n+1)]

    # O(nlogn):
    for i in range(n):  # O(n)
        idx = bin_search(A[i], N, n + 1)  # O(logn)
        N[idx] = min(A[i], N[idx])
        # P[idx].append((A[i], i))
        F[i] = idx

    maxLIS = max(F)
    printLIS(A, F, maxLIS, n-1)

    return maxLIS