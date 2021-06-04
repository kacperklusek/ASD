from random import randint, seed


class Node:
    def __init__(self):
        self.next = None
        self.value = None


def qsort(l):

    if l is None:
        return l
    elif l.next is None:
        return l

    greater = None
    equal = None
    less = None

    pivot = l
    l = l.next
    pivot.next = None
    equal = pivot

    # tworzenie list less, greater i equal
    while l is not None:
        tmp = l
        l = l.next
        if tmp.val < pivot.value:
            tmp.next = less
            less = tmp
        elif tmp.val == pivot.value:
            tmp.next = equal
            equal = tmp
        else:
            tmp.next = greater
            greater = tmp

    greater = qsort(greater)
    less = qsort(less)

    l = less
    if less:
        while less.next is not None:
            less = less.next
        less.next = equal
    else:
        l = equal
    while equal.next is not None:
        equal = equal.next
    equal.next = greater

    return l


def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X
    return H.next


def printlist(L):
    while L != None:
        print(L.value, "->", end=" ")
        L = L.next
    print("|")


seed(42)

n = 10
T = [randint(1, 10) for i in range(100)]
L = tab2list(T)

print("przed sortowaniem: L =", end=" ")
printlist(L)
L = qsort(L)
print("po sortowaniu    : L =", end=" ")
printlist(L)

if L == None:
    print("List jest pusta, a nie powinna!")
    exit(0)

P = L
while P.next != None:
    if P.value > P.next.val:
        print("Błąd sortowania")
        exit(0)
    P = P.next

print("OK")
