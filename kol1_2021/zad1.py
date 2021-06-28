from zad1testy import runtests


def partition(t, p, k):
    pivot = t[k]
    last = p-1
    for i in range(p, k):
        if t[i] <= pivot:
            last += 1
            t[last], t[i] = t[i], t[last]
    t[last+1], t[k] = t[k], t[last+1]
    return last+1


def select(t, k, p=0, r=None):
    if r is None: r = len(t)-1

    q = partition(t, p, r)
    if k < q:
        return select(t, k, p, q-1)
    elif k == q:
        return t[q]
    else:
        return select(t, k, q+1, r)


def linearize(tab):
    n = len(tab)
    output = []
    for i in range(n):
        output.extend(tab[i])
    return output


def Median(T):
    n = len(T)
    tab = linearize(T)

    # uzupełniam przekątną
    for i in range(n):
        T[i][i] = select(tab, int((n/2)*(n-1)) + i)

    # uzupełniam pod przekątną
    idx = 0
    for i in range(n):
        for j in range(i):
            T[i][j] = tab[idx]
            idx += 1

    # uzupełniam nad przekatna
    idx += n
    for i in range(n):
        for j in range(i+1, n):
            T[i][j] = tab[idx]
            idx += 1


runtests( Median ) 
