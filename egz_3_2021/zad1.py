from zad1testy import runtests

'''
korzystam z programowania dynamicznego
wykorzystuje trzy funkcje rekurencyjne

f[j][i] - najdłuższy podciąg (ściśle) rosnący kończąćy się na indeksie i i zaczynający na j
g[i] - najdłuższy podciąg (ściśle) malejący kończący się na indeksie i

m[i] - najdłuższy podciąg mr kończący się na indeksie i

'''


def bin_search(num, N, n):
    i = n//2
    l, r = 0, n-1
    while 1:
        if N[i] < num <= N[i + 1]:
            return i+1
        elif N[i] < num:
            l = i
        else:
            r = i

        i = (l+r)//2

def bin_search_decrease(num, N, n):
    i = n//2
    l, r = 0, n-1
    while 1:
        if N[i] > num <= N[i + 1]:
            return i+1
        elif N[i] < num:
            l = i
        else:
            r = i

        i = (l+r)//2

# F[i] - LIS konczacy sie na indeksie i
# N[i] - końcówka ciągu długości i (najmniejsza z możliwych)
# i - od kąd ma się zaczynać
def LIS(A, i=0):
    A = A[i:]
    n = len(A)
    m = max(A)
    F = [0] * n
    N = [m] * (n+1)
    N[0] = float('-inf')

    # O(nlogn)
    for i in range(n):
        idx = bin_search(A[i], N, n+1)
        N[idx] = min(A[i], N[idx])
        F[i] = idx

    return max(F)

# F[i] - LDS konczacy sie na indeksie i
# N[i] - końcówka ciągu długości i (najwieksza z możliwych)
def LDS(A):
    n = len(A)
    m = min(A)
    F = [0] * n
    N = [m] * (n+1)
    N[0] = float('inf')

    for i in range(n):
        idx = bin_search_decrease(A[i], N, n+1)
        N[idx] = max(A[i], N[idx])
        F[i] = idx

    return max(F)


def mr( X ):
    return 0

    
runtests( mr )


