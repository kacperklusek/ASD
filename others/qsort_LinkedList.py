from random import randint, seed
from time import time

class Node:
    def __init__(self, val=None, n=None):
        self.val = val
        self.next = n


def partition(A, end=None):
    if A is end: return A, A, A
    pivot = A
    pivot_end = A
    first = A
    prev = A

    A = A.next

    while A is not end:
        if A.val < pivot.val:
            prev.next = A.next
            A.next = first
            first = A
        elif A.val == pivot.val and pivot_end.next is not A:
            prev.next = A.next
            A.next = pivot_end.next
            pivot_end.next = A
            pivot_end = A
        else:
            prev = A

        A = prev.next

    return first, pivot, pivot_end


def quicksort(A, end=None):
    if A is not end:
        A, p_start, p_end = partition(A, end)
        A = quicksort(A, p_start)
        p_end.next = quicksort(p_end.next, end)

    return A


def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.val = A[i]
        C.next = X
        C = X
    return H.next


def printlist(L):
    while L != None:
        print(L.value, "->", end=" ")
        L = L.next
    print("|")


seed(42)

n = 1000000
T = [randint(1, n) for i in range(n)]
L = tab2list(T)
# printlist(L)
# L , s, t = partition(L)
# printlist(L)

start = time()
L = quicksort(L)
print(time() - start)

if L == None:
    print("List jest pusta, a nie powinna!")
    exit(0)

P = L
while P.next != None:
    if P.val > P.next.val:
        print("Błąd sortowania")
        exit(0)
    P = P.next

print("OK")
