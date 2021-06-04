from random import randint, seed
from lis_n2 import LIS

# Przechowuje w osobnej tablicy, końcówki ciągów o odpowiedniej długości: N[i] - końcówka ciągu długości i (najmniejsza
# z możliwych), dla każdej liczby w A szukam binarnie w N, indeksu i, dla którego (N[i] < A[j] and N[i+1] >= A[j]).
# A tak to zapisuję w tablicy F[i] najdłuższy rosnący podciąg kończący się na indeksie i


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


def LIS_turbo_s(A):
    n = len(A)
    m = max(A)       # O(n)
    F = [0] * n      # O(n)
    N = [m] * (n+1)  # O(n)
    N[0] = 0                # zakładając że liczby w A są > 0

    # O(nlogn)
    for i in range(n):   #O(n)
        idx = bin_search(A[i], N, n+1)  # O(logn)
        N[idx] = min(A[i], N[idx])
        F[i] = idx

    return max(F)


# ------- testy -------

seed(42)
n = 15
A = [randint(1, n*n) for _ in range(n)]
print(A)
print(LIS(A))
print(LIS_turbo_s(A))
