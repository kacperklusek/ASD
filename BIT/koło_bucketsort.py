from math import sqrt
from random import randint, shuffle, seed


def insertion(t):
    for d in range(0, len(t)-1):
        for i in range(d, -1, -1):
            if t[i][0]**2 + t[i][1]**2 > t[i+1][0]**2 + t[i+1][1]**2:
                t[i+1], t[i] = t[i], t[i+1]
            else:
                break


def circle(t, k):   # t - tablica wspolrzednych punktow; k - promien okregu
    n = len(t)
    buckets = [[] for _ in range(n)]
    # r1 = k / sqrt(n)
    const = ((k**2)/n)

    # wrzucanko do odpowiednich kubełków    O(n)
    for i in range(n):
        odl2 = t[i][0]**2 + t[i][1]**2
        buckets[int(odl2//const)].append(t[i])

    # sortowanko każdego kubełka    O(n) bo rozkład jednostajny
    for i in range(n):
        insertion(buckets[i])

    # wrzucanko do bazowej listy pososrtowanych już punktów z bucketsów     O(n)
    idx = 0
    for i in range(n):
        for j in range(len(buckets[i])):
            t[idx] = buckets[i][j]
            idx += 1


seed(42)
n = 5
le_t = 10 * n
points = [(randint(-n, n), randint(-n, n))for i in range(le_t)]
for i in range(le_t-1, -1, -1):
    if points[i][0]**2 + points[i][1]**2 >= n**2:
        points.pop(i)
print(points)
circle(points, n)
print(points)