from random import randint, seed, shuffle


def partition(t, p, k):
    pivot = t[k]
    last = p-1
    for i in range(p, k):
        if t[i] <= pivot:
            last += 1
            t[last], t[i] = t[i], t[last]
    t[last+1], t[k] = t[k], t[last+1]
    return last+1


def select(t, k, p=0, r=None):   # tablica t, czukamy elementu (liczby) na k-tej pozycji
    if r is None: r = len(t)-1

    q = partition(t, p, r)
    if k < q:
        return select(t, k, p, q-1)
    elif k == q:
        return t[q]
    else:
        return select(t, k, q+1, r)


seed(42)
n = 10

t = [4,3,5,7,8,3]
x = select(t, 3)
print(x)
# for i in range(n):
#     A = list(range(n))
#     shuffle(A)
#     print(A)
#     x = select(A, i)
#     if x != i:
#         print("Blad podczas wyszukiwania liczby", i)
#         # exit(0)
# print("OK")
