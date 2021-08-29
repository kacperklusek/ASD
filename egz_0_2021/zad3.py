from zad3testy import runtests


def jumper(G, s, w):
    def relax(u, v):
        nonlocal d, G, parent
        # wybieram najlepszego poprzednika do dwumilowego kroku (u jest wierzcholkiem miedzy poprzednikiem a v)
        for i in range(n):
            if G[u][i] and i != v:
                if d[i][0] + max(G[i][u], G[u][v]) < d[v][1]:
                    d[v][1] = d[i][0] + max(G[u][v], G[i][u])
                    parent[v][1] = i
        # relaksuje v zwykłym krokiem, mogę pójść albo z miejsca w którym skończyłem zwykły albo dwumilowy krok
        if d[u][0] + G[u][v] < d[v][0] or d[u][1] + G[u][v] < d[v][0]:
            d[v][0] = d[u][0] + G[u][v] if d[u][0] < d[u][1] else d[u][1] + G[u][v]
            parent[v][0] = u

    n = len(G)

    d = [[float("inf"), float('inf')] for _ in range(n)] # d[i][0] - ostatni krok był zwykły, d[i][1] - ostatni krok dwumilowy
    d[s][0] = d[s][1] = 0
    parent = [[-1, -1] for _ in range(n)]  # parent [0] to parent zwykłego kroku a parent[1] kroku dwumilowego
    processed = [0 for _ in range(n)]
    n_of_processed = 0

    while n_of_processed < n:
        # wybieram wierzchołek o najmniejszym oszacowaniu d[u][]  O(V)
        u = -1
        for i in range(n):
            if not processed[i]:
                if u == -1 or min(d[i]) < min(d[u]):
                    u = i
                elif u == -1 or min(d[i]) == min(d[u]):
                    if u == -1 or d[i][0] == min(d[u]):
                        u = i if u == -1 or d[i][1] < max(d[u]) else u
                    else:
                        u = i if d[i][0] < max(d[u]) else u
        # wybrałem wierzchołek

        # relaksacja
        for v in range(n):
            if not processed[v] and G[u][v] != 0 and v != parent[u][0] and v != parent[u][1]:
                relax(u, v)

        processed[u] = 1
        n_of_processed += 1

    return min(d[w])


runtests(jumper)
