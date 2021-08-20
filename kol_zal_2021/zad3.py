from zad3testy import runtests
from queue import PriorityQueue

'''
f[i][j] - najmniejsza liczba tankowań, potrzebna by dojechać do i-tej stacji, mając j litrów paliwa

pomijam przypadki tankowania więcej niż l litrów paliwa (bez sensu)
zatem f[i][j] opiera się o dwuwymiarową macierz rozmiarów rzędu n x q
'''


def iamlate(T, V, q, l):
    if T[1] > min(V[0], q) or sum(V) < l:
        return []

    # dodaje ostatnią syntetyczną stacje, będącą końcem drogi
    T.append(l)
    V.append(0)

    n = len(T)

    # poprawiam pojemności stacji, żeby nie były za duże
    for i in range(n):
        V[i] = min(V[i], q)


    f = [[float('inf') for _ in range(q+1)] for __ in range(n)]

    for i in range(V[0] + 1):
        f[0][i] = 1

    def foo(i, j):
        nonlocal f, T, V, q, l
        if 0 > i or i >= n or j < 0 or j > q:
            return float('inf')
        elif f[i][j] < float('inf'):
            return f[i][j]
        else:
            z = T[i]-T[i-1]
            val = float('inf')

            # bez tankowania w obecnej stacji
            val = foo(i-1, z + j)

            # z tankowaniem w obecnej stacji
            for m in range(V[i]):
                val = min(val, foo(i-1, j + z - m) + 1)

            f[i][j] = val
            return f[i][j]

    x = foo(n-1, 0)

    return []


runtests( iamlate )
