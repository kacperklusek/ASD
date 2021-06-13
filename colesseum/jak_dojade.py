def dijkstra(G, s):
    def relax(u, v):
        nonlocal d, G, parent
        if d[v] > d[u] + G[u][v]:
            d[v] = d[u] + G[u][v]
            parent[v] = u

    n = len(G)

    # s - wierzchołek startowy

    d = [float("inf") for _ in range(n)]
    d[s] = 0
    parent = [-1 for _ in range(n)]
    processed = [0 for _ in range(n)]
    n_of_processed = 0

    while n_of_processed < n:
        # wybieram wierzchołek o najmniejszym oszacowaniu O(V)
        u = -1
        for i in range(n):
            if not processed[i] and (u == -1 or d[i] < d[u]):
                u = i

        # relaksuje sąsiadów
        for v in range(n):
            if not processed[v] and G[u][v] != -1 and v != parent[u]:
                relax(u, v)

        processed[u] = 1
        n_of_processed += 1

    return d, parent   # tablica odległości i parentów


def jak_dojade(G, P, z, a, b):
    n = len(G)
    g = len(P)

    # graf przechowujący możliwe odl, między stacjami i pkt końcowym
    G2 = [[-1 for _ in range(n)] for __ in range(n)]
    path = [[[] for _ in range(n)] for __ in range(n)]

    for i in range(g):
        d, parent = dijkstra(G, P[i])

        for j in range(g):
            G2[P[i]][P[j]] = d[P[j]] if d[P[j]] <= z else -1
        G2[P[i]][b] = d[b] if d[b] <= z else -1

        for j in range(n):
            if P[i] == j or d[j] > z:
                continue
            aux = j
            while parent[aux] != -1:
                path[P[i]][j].append(aux)
                aux = parent[aux]


    # znajduję najkrótszą drogę w skonwertowanym grafie
    d, parent = dijkstra(G2, a)
    output = []
    aux = b
    while parent[aux] != -1:
        output.extend(path[parent[aux]][aux])
        aux = parent[aux]
    output.append(a)

    output.reverse()

    return output if len(output)>1 else None


# TESTY ###########################################################################

import copy

G1 = [[-1, 5, -1, 2], [-1, -1, -1, -1], [5, -1, -1, 5], [2, 2, -1, -1]]
P1 = [2, 0]
L1 = 9
# a=2, b=1, d=6

G2 = [[-1, 2, -1, -1, 3], [2, -1, 2, -1, -1], [-1, 2, -1, 2, -1], [-1, -1, 2, -1, 3], [3, -1, -1, 3, -1]]
P2 = [0, 2]
L2 = 6
# a=0, b=3, d=4

G3 = [[-1, 3, -1, 5, -1, 2], [3, -1, 4, -1, -1, -1], [-1, 4, -1, 6, -1, -1], [-1, -1, 6, -1, 2, -1],
      [-1, 5, -1, 2, -1, 3], [2, -1, -1, -1, 3, -1]]
P3 = [0, 4, 5]
L3 = -1
# a=5, b=2, d=5


TESTS = [(G1, P1, 6, 2, 1, L1),
         (G2, P2, 4, 0, 3, L2),
         (G3, P3, 5, 5, 2, L3)]


def isok(G, P, d, a, b, path, exp_len):
    if exp_len < 0 and path == None:
        print("Brak sciezki, zgodnie z oczekiwaniem")
        return True
    if exp_len >= 0 and path == None:
        print("Rozwiazanie nie zwrocilo sciezki, mimo ze taka istnieje")
        return False

    if path[0] != a:
        print("Rozwiazanie zwraca bledny poczatek sciezki")

    tank = d
    sol_len = 0
    v = a
    for u in path[1:]:
        if G[v][u] < 0:
            print("Nie istnieje krawedz z %d to %d" % (v, u))
            return False
        tank -= G[v][u]
        sol_len += G[v][u]
        if tank < 0:
            print("Zabraklo benzyny na krawedzi z %d do %d" % (v, u))
            return False
        v = u
        if v in P:
            tank = d

    print("Dlugosc otrzymanej trasy =", sol_len)
    if sol_len > exp_len:
        print("Za dluga trasa!")
        return False

    return True


def runtests(f):
    OK = True
    for (G, P, d, a, b, L) in TESTS:
        res = f(copy.deepcopy(G), copy.deepcopy(P), d, a, b)
        print("----------------------")
        print("G =")
        for i in range(len(G)): print(G[i])
        print("P =", P)
        print("d = ", d)
        print("a = ", a)
        print("b = ", b)
        print("otrzymany wynik  =", res)
        print("oczekiwana dlugosc trasy =", L)

        if not isok(G, P, d, a, b, res, L):
            print("Blad!")
            OK = False
        else:
            print()
    print("----------------------")

    if OK:
        print("OK!")
    else:
        print("Bledy!")

runtests(jak_dojade)