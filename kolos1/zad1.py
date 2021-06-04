# KACPER KŁUSEK
# DZIAŁANIE PROGRAMU:
# wybierając pierwszy i ostatni element na przekątnej za pomocą funkcji select [pozycje (n**2 - n)//2 i (2**2 - n)//2 + n - 1]
# możemy liniowo przejść po tablicy i wstawić resztę elementów między te wartości
# następnie wypełniamy 'boki' tablic (prawa i lewa strona głównej przekątnej) pozostałymi liczbami odpowiednio więksymi po prawej
# i mniejszymi po lewej


from zad1testy import runtests


#
#
# def partition(t, p, k):
#     n = len(t)
#     k1, k2 = get_idx_in_tab(k, n)
#     pivot = t[k1][k2]
#     last1, last2 = get_idx_in_tab(p - 1, n)
#     for i in range(p, k):
#         i1, i2 = get_idx_in_tab(i, n)
#         if t[i1][i2] <= pivot:
#             last1 = (last1 + 1) % n
#             last2 += 1 if last1 == 0 else 0
#             t[last1][last2], t[i1][i2] = t[i1][i2], t[last1][last2]
#     last1 = (last1 + 1)%n
#     last2 += 1 if last1 == 0 else 0
#     t[last1][last2], t[k1][k2] = t[k1][k2], t[last1][last2]
#     return last1, last2
#
#
# def select(t, k, p=0, r=None):   # tablica t, czukamy elementu (liczby) na k-tej pozycji
#     n = len(t)
#     if r is None: r = len(t)**2 - 1
#
#     q1, q2 = partition(t, p, r)
#     if k < get_flat_idx(q1, q2, n):
#         q = get_flat_idx(q1, q2, n)
#         return select(t, k, p, q-1)
#     elif k == get_flat_idx(q1, q1, n):
#         return t[q1][q2]
#     else:
#         q = get_flat_idx(q1, q2, n)
#         return select(t, k, q+1, r)

def get_idx_in_tab(n, size):          # linearyzuje wyszukiwanie w tablicy
    return n//size, n % size


def get_flat_idx(i1, i2, n):
    return i1*n + i2


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


def Median(T):
    n = len(T)
    new_tab = []

    for i in range(n):
        for j in range(n):
            new_tab.append(T[i][j])

    first = select(new_tab, (n**2 - n)//2)    # pierwszy element na głównej przekątnej
    last = select(new_tab, (n**2 - n)//2 + n - 1)     # ostatni element na głównej przekątnej

    new = len(new_tab)
    w = 0
    for i in range(new):
        if last > new_tab[i] > first:
            T[w][w] = new_tab[i]

        elif new_tab[i] < first:





Median([[1,2],[3,4]])


runtests( Median )