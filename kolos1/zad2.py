# KACPER KŁUSEK
# działanie algorytmu:
# algorytm przechodzi po liście pamiętając sortując po kolei k+1 elementów, bo w najgorszym przypadku każdy element byłby
# oddalony od swojej pozycji o k miejsc, sortuje quicksortem
# dla k = O(1) algorytm działa w O(n) bo sortowanie jest w czasie jednostkowym
# dla k = O(logn) algorytm działa w O(n*log^2(logn))
# dla k = O(n) algorytm działa w O(nlogn) bo jest to po prostu quicksort
# złożoność algorytmu to O(n*klog(k))


from zad2testy import runtests


class Node:
    def __init__(self):
        self.val = None
        self.next = None


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


def SortH(p, k):
    if k == 0:
        return p

    temp = p
    for i in range(k + 1):
        if temp is not None:
            temp = temp.next

    stop = temp
    p = quicksort(p, stop)
    first = p
    if stop is None:
        pass
    else:
        stop = stop.next
        while stop is not None:
            first.next = quicksort(first.next, stop)
            first = first.next
            stop = stop.next

    first.next = quicksort(first.next, stop)

    return p


runtests( SortH )
