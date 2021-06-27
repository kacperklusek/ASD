from zad3testy import runtests
from math import log


def insertion(t):
    for d in range(len(t)-1):
        for i in range(d, -1, -1):
            if t[i] > t[i+1]:
                t[i+1], t[i] = t[i], t[i+1]
            else:
                break
    return t


def fast_sort(tab, a):
    n = len(tab)
    buckets = [[] for _ in range(n+1)]

    # math.log(x, base)

    for i in range(n):
        buckets[int(log(tab[i], a)*n)].append(tab[i])

    for i in range(n):
        buckets[i] = insertion(buckets[i])

    i = 0
    for bucket in buckets:
        for elem in bucket:
            tab[i] = elem
            i += 1

    return tab
    

runtests(fast_sort)
