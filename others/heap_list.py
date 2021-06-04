from math import log2

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
    if l < n and A[l] > A[m]: m = l
    if r < n and A[r] > A[m]: m = r

    if m != i:
        swap(A, i, m)
        heapify(A, n, m)


def buildheap(A):
    n = len(A)
    for i in range(parent(n), -1, -1):
        heapify(A, n, i)


def insert(A, val):
    A.append(val)
    n = len(A)
    i = n-1
    while A[parent(i)] < A[i]:
        swap(A, parent(i), i)
        i = parent(i)


def heapsort(A):
    n = len(A)
    buildheap(A)
    for i in range(n-1, 0, -1):
        swap(A, 0, i)
        heapify(A, i, 0)


def prnt_heap(A):
    e = 0
    count = 0
    d = int(log2(len(A)))
    for i in range(len(A)):
        tab = d - e + 1
        print("  " * tab, A[i], end='')
        count += 1
        if 2**e == count:
            e += 1
            count = 0
            print()



heap = [2, 1, 7, 10, 12, 17, 42, 13, 19, 22]

buildheap(heap)
insert(heap, 20)
print(heap)
prnt_heap(heap)
