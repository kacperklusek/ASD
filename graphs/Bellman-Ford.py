# negative edge wieghts
# O(V³)

def bellman_ford(G, s=0, t=1):
    n = len(G)

    def relax(u, v):
        nonlocal G, d
        if d[v] > d[u] + G[u][v]:
            d[v] = d[u] + G[u][v]
            parent[v] = u

    # inicjalizacja
    parent = [-1 for _ in range(n)]
    d = [float('inf') for _ in range(n)]
    d[s] = 0

    # relaksacje
    for i in range(n):
        for u in range(n):
            for v in range(n):
                if G[u][v] != 0:    # 0 lub inna forma reprezentacji braku krawędzi na grafie w repr. macierzowej
                    relax(u, v)

    # weryfikacja
    for u in range(n):
        for v in range(n):
            if G[u][v] != 0 and d[v] > d[u]+G[u][v]:
                # mamy cykl ujemny
                return None

    return d # d- tablica krawędzi

