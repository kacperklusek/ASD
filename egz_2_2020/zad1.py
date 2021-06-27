from zad1testy import runtests


def zbigniew( A ):
    n = len(A)

    f = [[float('inf') for _ in range(n)] for __ in range(n)]

    f[0][A[0]] = 0

    # poniższa część kodu wykona się nie więcej niz O(n²) razy
    for i in range(n):
        for j in range(1, n):
            if f[i][j] < float('inf'):
                for r in range(i+1, min(n, i+j + 1)):
                    f[r][min(n-1, j - (r-i) + A[r])] = min(f[i][j] + 1, f[r][min(n-1, j- (r-i) + A[r])])

    return min(f[n-1])

       

runtests( zbigniew ) 
