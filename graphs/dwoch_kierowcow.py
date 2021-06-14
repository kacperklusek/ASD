def two_riders_of_the_storms(G, s, t):
    def relax(u, v):
        nonlocal d, G, parent_n, parent_j
        if d[u][1] + G[u][v] < d[v][0]:
            d[v][0] = d[u][1] + G[u][v]
            parent_j[v] = u
        if d[u][0] < d[v][1]:
            d[v][1] = d[u][0]
            parent_n[v] = u

    n = len(G)

    # s = 0   # wierzchołek startowy

    d = [[float("inf"), float("inf")] for _ in range(n)]
    d[s] = [0, 0]
    parent_j = [-1 for _ in range(n)]
    parent_n = [-1 for _ in range(n)]
    parent_n[s] = parent_j[s] = -1
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
        # wybrałem wierzchołek o najmniejszych wartościach

        # relaksacja
        for v in range(n):  # \/ powinno być ok ale jakby
            # if G[u][v] != 0 and v != parent_j[u] and v != parent_n[u]:   # \/ nie działało to zmienić warunek na ten
            if not processed[v] and G[u][v] != 0 and v != parent_j[u] and v != parent_n[u]:
                relax(u, v)

        processed[u] = 1
        n_of_processed += 1

    aux = t
    path = [aux]
    ride = True if d[t][1] < d[t][0] else False

    while parent_n[aux] != -1 and parent_j[aux] != -1:
        if not ride:  # tzn. że najkrótsza droga to taka, że krawędź (parent_j[end], end) alicja prowadziła
            aux = parent_j[aux]
            ride = True
        else:  # tzn. że najkrótsza droga to taka, że krawędź (parent_n[end], end) alicja nie prowadziła
            aux = parent_n[aux]
            ride = False
        path.append(aux)

    path.reverse()

    return path, ride, min(d[t])


# testy

G = [[0, 5, 0, 0, 0, 0, 0, 0, 7],
     [5, 0, 3, 0, 0, 0, 0, 2, 0],
     [0, 3, 0, 4, 0, 0, 0, 0, 0],
     [0, 0, 4, 0, 3, 0, 1, 0, 0],
     [0, 0, 0, 3, 0, 2, 0, 0, 0],
     [0, 0, 0, 0, 2, 0, 2, 0, 6],
     [0, 0, 0, 1, 0, 2, 0, 5, 0],
     [0, 2, 0, 0, 0, 0, 5, 0, 3],
     [7, 0, 0, 0, 0, 6, 0, 3, 0],
     ]

path, ride, dist = two_riders_of_the_storms(G, 0, 4)
print(path, f"dist = {dist}")
print(f'alicja {"" if ride else "nie "}powinna jechać pierwsza')

G1 = [[0, 2, 4, 0],
      [2, 0, 3, 0],
      [4, 3, 0, 1],
      [0, 0, 1, 0],
      ]

path1, ride1, dist1 = two_riders_of_the_storms(G1, 0, 3)
print(path1, f"dist = {dist1}")
print(f'alicja {"" if ride1 else "nie "}powinna jechać pierwsza')
