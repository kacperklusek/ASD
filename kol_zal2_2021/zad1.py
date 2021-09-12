from zad1testy import runtests


def partition(t, p, k, j):
    pivot = t[k][j]
    last = p-1
    for i in range(p, k):
        if t[i][j] <= pivot:
            last += 1
            t[last], t[i] = t[i], t[last]
    t[last+1], t[k] = t[k], t[last+1]
    return last+1


def select(t, k, j, p=0, r=None):   # tablica t, czukamy elementu (liczby) na k-tej pozycji
    if r is None: r = len(t)-1

    q = partition(t, p, r, j)
    if k < q:
        return select(t, k, j, p, q-1)
    elif k == q:
        return t[q][j]
    else:
        return select(t, k, j, q+1, r)


def rect(D):
    n = len(D)

    Dcpy = D[:]

    left = max(D, key=lambda x: x[0])[0]
    right = min(D, key=lambda x: x[2])[2]
    up = min(D, key=lambda x: x[3])[3]
    down = max(D, key=lambda x: x[1])[1]
    left_prev = select(D, n-2, 0)
    right_prev = select(D, 1, 2)
    up_prev = select(D, 1, 3)
    down_prev = select(D, n-2, 1)

    D = Dcpy

    # sprawdzam czy wszystko okej
    if left < right and up > down:
        S = (right - left) * (up - down)
    else:
        S = 0

    Smax = S
    to_delete = -1

    for i in range(n):
        l, d, r, u = D[i]

        nw = [left_prev if l == left else left,
              down_prev if d == down else down,
              right_prev if r == right else right,
              up_prev if u == up else up]

        if nw[0] < nw[2] and nw[1] < nw[3]:
            Snew = (nw[2] - nw[0]) * (nw[3] - nw[1])
        else:
            Snew = 0
        
        if Snew > Smax:
            to_delete = i
            Smax = Snew

    return to_delete





runtests( rect )


