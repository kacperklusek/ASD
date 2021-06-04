from random import randint, seed


class Node:
    def __init__(self):
        self.next = None
        self.value = None


def partition(piv, stop):
    if piv is stop:
        return piv, piv, piv, stop
    if piv.next is stop:
        return piv, piv, piv.next, stop

    less = Node()
    less.next = piv
    greater = Node()            # less -> piv -> greater -> END=stop
    greater.next = stop
    equal = piv
    j = piv.next
    piv.next = greater
    while j is not stop:
        tmp = j
        j = j.next
        if tmp.value > piv.val:
            if not greater.value:
                greater = tmp
                piv.next = greater
                greater.next = stop
            else:
                greater.next = tmp
                greater = greater.next
                greater.next = stop
        elif tmp.value < piv.val:
            if not less.value:
                less = tmp
                less.next = piv
            else:
                tmp.next = less
                less = tmp
        else:
            equal.next, tmp.next = tmp, equal.next
            equal = equal.next

    return less, piv, equal.next, stop


def qsort(l, end=None):
    if l is not end:
        l, piv, g, stop = partition(l, end)
        qsort(l, piv)
        qsort(g, stop)

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
T = [randint(1, 10) for i in range(5)]
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
    if P.val > P.next.val:
        print("Błąd sortowania")
        exit(0)
    P = P.next

print("OK")
# printlist(L)
# l, p, g, stop = partition(L, stop=None)
# printlist(l)
# printlist(p)

