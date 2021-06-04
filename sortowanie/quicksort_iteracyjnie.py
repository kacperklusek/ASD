from random import randint, seed


def partition(T, l, r):
    last = l
    for i in range(l, r):
        if T[i] <= T[r]:
            T[i], T[last] = T[last], T[i]
            last += 1
    T[last], T[r] = T[r], T[last]
    return last


def partition_hoare(T, l, r):
    p = T[r]
    piv = r
    r -= 1
    while l < r:
        if T[l] > p > T[r]:
            T[l], T[r] = T[r], T[l]
            l += 1
            r -= 1
        else:
            if T[l] <= p: l += 1
            if T[r] >= p: r -= 1
    z = l if T[l] > p else l + 1
    T[z], T[piv] = T[piv], T[z]
    return z


def quicksort(T):
    n = len(T)
    stack = []
    stack.append((0, n - 1))
    while stack:
        l, r = stack.pop()
        if l < r:
            q = partition(T, l, r)
            stack.append((l, q - 1))
            stack.append((q + 1, r))

seed(42)
t = [randint(1, 99) for _ in range(20)]
t1 = t[:]
print(t)
t1.sort()
quicksort(t)
print(t)
print(t1)
