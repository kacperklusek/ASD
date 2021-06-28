from zad3testy import runtests


def bubble(t):
    for k in range(len(t) - 1):
        for i in range(len(t) - 1 - k):
            if t[i] > t[i + 1]:
                t[i], t[i + 1] = t[i + 1], t[i]

    return t


def bucket_sort(T, u, v):
    n = len(T)
    rng = (v-u) / n
    buckets = [[] for _ in range(n)]

    for i in range(n):
        buckets[int((T[i]-u) / rng)].append(T[i])

    for i in range(n):
        buckets[i] = bubble(buckets[i])

    idx = 0
    for i in range(n):
        for j in range(len(buckets[i])):
            T[idx] = buckets[i][j]
            idx += 1

    return T


def SortTab(T,P):
    k = len(P)
    n = len(T)

    P = [[P[i][0], P[i][1]] for i in range(k)]
    buckets = [[] for _ in range(k)]

    # żeby przedzały na siebie nie nachodziły
    for i in range(k-1):
        P[i][1] = min(P[i+1][0], P[i][1])

    # dla każdego elementu z T wsadzam go do bucketa
    for i in range(n):
        for j in range(k):
            if P[j][0] <= T[i] < P[j][1]:
                buckets[j].append(T[i])
                break

    # dla każdego bucketa sortuje go bucket sortem
    for i in range(k):
        u, v = P[i]
        buckets[i] = bucket_sort(buckets[i], u, v)

    # scalam nową posortowaną tablicę
    idx = 0
    for i in range(k):
        for j in range(len(buckets[i])):
            T[idx] = buckets[i][j]
            idx += 1

    return T



runtests( SortTab )