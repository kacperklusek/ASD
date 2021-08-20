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


    f = [[[] for _ in range(q+1)] for __ in range(n)]


    for i in range(V[0] + 1):
        f[0][i] = [0]

    for i in range(1, n):
        for j in range(q+1):
            # z - odległość do poprzedniej stacji
            z = T[i] - T[i-1]

            # przypadek, w którym nie muszę tankować na obecnej stacji
            if j+z <= q:
                f[i][j] = f[i-1][j+z]

            # przypadki, gdzie dotankowuje k paliwa na obecnej (i-tej) stacji
            for k in range(1, V[i] + 1):
                if j + z - k <= q:
                    if f[i][j] == [] or len(f[i-1][j + z - k]) + 1 < len(f[i][j]):
                        # sprawdzam jeszcze, czy mogłem dojechać wcześniej na i-1 stacje z j+z-k paliwa
                        # oraz czy nie tankuje więcej niż chce mieć paliwa (ujemna wartość w baku)
                        if f[i - 1][j + z - k] and j >= k:
                            f[i][j] = f[i - 1][j + z - k] + [i]

    f[n - 1][0].sort()

    return f[n-1][0]


runtests( iamlate )
