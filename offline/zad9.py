from copy import deepcopy


# KACPER KŁUSEK
# opis algorytmu:
# usuwam jedną krawędź z grafu, następnie algorytmem Dijkstry szukam najmniejszej odległości pomiędzy
# wierzchołkami, które były połączone tą krawędzią, jeśli istnieje ścieżka między tymi krawędziami (najkrótsza),
# to dodaję do niej usuniętą krawędź tworząc cykl.
# powtarzam powyższy krok dla każdej krawędzi w grafie
#
# złożoność obliczeniowa to: O(EV²), gdzie E i V to odpowiednio liczba krawędzi i wierzchołków
# używam wersji algortmu Dijkstry o złożoności O(V²)


def min_cycle(G):
    def relax(u, v):
        nonlocal d, G, parent
        if d[v] > d[u] + G[u][v]:
            d[v] = d[u] + G[u][v]
            parent[v] = u

    n = len(G)

    result = [[], float('inf')]

    for s in range(n):                      # tu wyznaczam krawędzi do sprawdzenia, każdą sprawdzam tylko raz
        for phantom in range(s + 1, n):     #
            if G[s][phantom] == -1:
                continue
            # kod poniżej wykona się tylko E razy, zw względu na ifa wyżej,
            # dlatego można oszacować złożoność przez O(V²+EV²) = O(EV²)

            # delete phantom edge
            phantom_weight = G[s][phantom]
            G[s][phantom] = G[phantom][s] = -1

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

                processed[u] = 1
                n_of_processed += 1

            # restore phantom edge
            G[s][phantom] = G[phantom][s] = phantom_weight

            # construe path (if exist)
            if d[phantom] != -1 and d[phantom] + G[s][phantom] < result[1]:
                path = [phantom]
                end = phantom
                while parent[end] != -1:
                    path.append(parent[end])
                    end = parent[end]
                result = [path, d[phantom] + G[s][phantom]]

    return result[0]


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
