from zad2testy import runtests

# złożoność O(nlogk)


class Node:
    def __init__(self):
        self.val = None
        self.next = None


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
    if l < n and A[l].val < A[m].val: m = l
    if r < n and A[r].val < A[m].val: m = r

    if m != i:
        swap(A, i, m)
        heapify(A, n, m)


def insert(A, value):
    A.append(value)
    n = len(A)
    i = n-1
    while A[parent(i)].val > A[i].val:
        swap(A, parent(i), i)
        i = parent(i)

def insert_no_append(A, value):
    n = len(A)
    A[n-1] = value
    i = n-1
    while A[parent(i)].val > A[i].val:
        swap(A, parent(i), i)
        i = parent(i)


def SortH(p: Node, k):

    Q = []
    for i in range(k+1):
        insert(Q, p)
        p = p.next

    new = Node()
    output = new

    while p is not None:  # O(n)
        swap(Q, 0, k)     # O(1)
        heapify(Q, k, 0)    # O(logk)
        new.next = Q[k]
        new = new.next
        insert_no_append(Q, p)  # O(logk)
        p = p.next

    for i in range(k, -1, -1):
        swap(Q, 0, i)
        heapify(Q, i, 0)
        new.next = Q[i]
        new = new.next

    new.next = None

    return output.next


runtests(SortH)
