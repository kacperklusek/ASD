from random import randint, seed
import time


def mergesort(T):
    if len(T) <= 1:
        return T
    m = len(T) // 2
    l1 = mergesort(T[m:])
    l2 = mergesort(T[:m])
    i1 = i2 = 0

    while i1 < len(l1) and i2 < len(l2):
        if l1[i1] <= l2[i2]:
            T[i1 + i2] = l1[i1]
            i1 += 1
        else:
            T[i1 + i2] = l2[i2]
            i2 += 1

    while i1 < len(l1):
        T[i1 + i2] = l1[i1]
        i1 += 1
    while i2 < len(l2):
        T[i1 + i2] = l2[i2]
        i2 += 1

    return T


seed(42)

n = 10
T = [randint(1, n) for i in range(n)]

print("przed sortowaniem: T =", T)
T = mergesort(T)
print("po sortowaniu    : T =", T)
for i in range(len(T) - 1):
    if T[i] > T[i + 1]:
        print("Błąd sortowania!")
        exit()

print("OK")
