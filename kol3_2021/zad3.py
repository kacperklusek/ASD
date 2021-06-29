from zad3testy import runtests
from zad3EK    import edmonds_karp

# zakładam że odległość między p i q (liczona jako suma wag krawędzi najkrótszej ścieżki) jest nie mniejsza niż d,
# najpierw usuwam krawędzie, które są dłuższe od D
# potem tworząc super źródło oraz super ujśćie znajduje największy przepływ czyli ilość krawędzi o które jestem proszony
# w poleceniu
# O(VE²) ze względu na metode Edmondsa-Karpa
#

def floyd_warshall(G):
    n = len(G)

    d = [[G[i][j] if G[i][j] > 0 else float('inf') for i in range(n)] for j in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    return d

def BlueAndGreen(T, K, D):
    n = len(T)

    d = floyd_warshall(T)
    for i in range(n):
        for j in range(n):
            if d[i][j] < D and T[i][j] > 0:
                T[i][j] = T[j][i] = 0
            elif d[i][j] >= D and T[i][j] == 0:
                T[i][j] = T[j][i] = 1

    G = [[0 for _ in range(n+2)]for __ in range(n+2)]
    for i in range(n):
        for j in range(n):
            G[i][j] = n*T[i][j]

    source = n
    sink = n+1
    for i in range(n):
        if K[i] == 'B':
            G[source][i] = G[i][source] = 1
        else:
            G[sink][i] = G[i][sink] = 1

    result = edmonds_karp(G, source, sink)

    return result

runtests( BlueAndGreen ) 
