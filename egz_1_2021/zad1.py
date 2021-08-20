from zad1testy import runtests

# opis algorytmu:
# wrzucam wszystkie wierzchołki do kolejki priorytetowej, i na bierząco w kolejnej pętli sprawdzam, jaka jest maksymalna
# 'odległość' od prawidłowej pozycji danego elementu, tym samym otrzymując k
# przy powtórzeniach nie będzie problemu, ponieważ w kolejne element (val:2, idx:3) będzie wcześniej niż element
# (val:2, idx:5)
# złożoność obliczeniowa algorytmu to O(nlogn)


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def swap(A, i1, i2):
    A[i1], A[i2] = A[i2], A[i1]


def parent(i):
    return i//2


def heapify(A, n, i):
    l = left(i)
    r = right(i)

    m = i
    if l < n and (A[l][0] < A[m][0] or (A[l][0] == A[m][0] and A[l][1] < A[m][1])): m = l
    if r < n and (A[r][0] < A[m][0] or (A[r][0] == A[m][0] and A[r][1] < A[m][1])): m = r

    if m != i:
        swap(A, i, m)
        heapify(A, n, m)


def insert(A, val):
    A.append(val)
    n = len(A)
    i = n-1
    while A[parent(i)][0] > A[i][0] or (A[parent(i)][0] == A[i][0] and A[parent(i)][1] > A[i][1]):
        swap(A, parent(i), i)
        i = parent(i)


def chaos_index( T ):
    n = len(T)

    Q = []

    for i in range(n):
        insert(Q, (T[i], i))

    k = 0
    for i in range(n):
        val, idx = Q[0]
        swap(Q, 0, n-1-i)
        heapify(Q, n-1-i, 0)
        k = max(k, abs(i-idx))

    return k



runtests( chaos_index )
