from copy import deepcopy


# KACPER KŁUSEK
# opis algorytmu:
# Dla każdego wierzchołka v wywołuję algorytm dijkstry. Zakładając że graf posiada optymalny cykl, to w końcu zdarzy
# się że będziemy rozważać wywołanie dla wierzchołka należącego do tego cyklu, to z definicji znajdzie nam najkrótszą
# ścieżkę do każdego z wierzchołków należących do tego cyklu.
# Długością cyklu jest oszacowanie przez d[u] + d[v] + G[u][v], gdzie u i v to sąsiedzi a d[u] i d[v] to odległość
# tych punktów od wierzchołka startowego s. W przypadku rozpatrywania s, u i v, które należą do optymalnego cyklu,
# oszacowanie to jest dokładnym wynikiem czyli długością optymalnego cyklu.
#
# TL;DR: Dijkstra dla każdego wierzchołka v, potencjalny cykl gdy sąsiadem rozpatrywanego wierzchołka u jest już
# oszacowany wierzchołek j. odtwarzam wynik przez pola parent.
#
# złożoność: O(V³) - V * algorytm dijksry O(V²)


def reconstruct_path(parent, u, v):
    path = []
    while parent[u] != -1:
        path.append(u)
        u = parent[u]
    path.reverse()
    path.append(v)
    while parent[v] != -1:
        v = parent[v]
        path.append(v)

    return path


def min_cycle(G):
    def relax(u, v):
        nonlocal d, G, parent
        if d[v] > d[u] + G[u][v]:
            d[v] = d[u] + G[u][v]
            parent[v] = u

    n = len(G)

    result = [[], float('inf')]
    path = []
    path_weight = float('inf')

    for s in range(n):
        # just dijkstra
        d = [float('inf') for _ in range(n)]
        d[s] = 0
        parent = [-1 for _ in range(n)]
        processed = [0 for _ in range(n)]
        n_of_processed = 0

        while n_of_processed < n:
            # wybieram wierzchołek nieprzetworzony z najmniejszym oszacowaniem d
            u = -1
            for i in range(n):
                if not processed[i] and (u == -1 or d[i] < d[u]):
                    u = i

            for v in range(n):
                if not processed[v] and G[u][v] != -1 and v != parent[u]:
                    relax(u, v)
                elif processed[v] and G[u][v] != -1 and v != parent[u]:
                    if result[1] >= d[u] + d[v] + G[u][v]:
                        result[1] = d[u] + d[v] + G[u][v]
                        result[0] = [parent, u, v]

            processed[u] = 1
            n_of_processed += 1

        if result[1] <= path_weight and result[0]:  # if result[0] <=> czy jest w ogóle cykl
            path_weight = result[1]
            maybe = reconstruct_path(*result[0])
            if path == [] or len(maybe) < len(path):
                path = maybe

    return path


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik


G = [[-1, 2, -1, -1, 1],
     [2, -1, 4, 1, -1],
     [-1, 4, -1, 5, -1],
     [-1, 1, 5, -1, 3],
     [1, -1, -1, 3, -1]]
LEN = 7

GG = deepcopy(G)
cycle = min_cycle(GG)

print("Cykl :", cycle)

if cycle == []:
    print("Błąd (1): Spodziewano się cyklu!")
    exit(0)

L = 0
u = cycle[0]
for v in cycle[1:] + [u]:
    if G[u][v] == -1:
        print("Błąd (2): To nie cykl! Brak krawędzi ", (u, v))
        exit(0)
    L += G[u][v]
    u = v

print("Oczekiwana długość :", LEN)
print("Uzyskana długość   :", L)

if L != LEN:
    print("Błąd (3): Niezgodna długość")
else:
    print("OK")
