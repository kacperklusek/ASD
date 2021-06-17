from zad1testy import runtests
from queue import Queue


# najpierw obliczam odległości między każdą parą wierzchołków
# następnie tworze graf, w którym wierzchołki to możliwe pozycje Carol i Maxa, a krawędź między odpowiednimi wierzchoł-
# kami (x, y) i (a, b) znaczy że można przejść z pozycji x,y do a,b w jednym ruchu zgodnie z zasadami (odległość)
# następnie sprawdzam czy istnieje ścieżka między wierzchołkami (x,y) a (y,x) w tym grafie i jeśli istnieje, to ją
# odtwarzam i zwracam (istnieje zawsze zgodnie z poleceniem)
# złożoność algorytmu to O(V^4) bo graf ma O(V²) wierzchołkówm gdzie V to liczba wierczhołków w grafie M przekazywanym
# jako argument

def floyd_warshall(G):
    n = len(G)

    d = [[G[i][j] if G[i][j] > 0 else float('inf') for i in range(n)] for j in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    return d


def keep_distance(M, x, y, d):
    n = len(M)
    dist = floyd_warshall(M)

    # graf możliwych położeń carol i maxa
    G = [[[[0 for _ in range(n)] for __ in range(n)] for ___ in range(n)] for ____ in range(n)]

    Q = Queue()
    Q.put((x, y))

    # wypełniam graf, krawędź miedzy (x,y) i (a, b) znaczy że można zmienić pozycje z x,y na a,b w jednym ruchu zgodnie
    # z zasadą że odległość ma być zawsze >= d
    while not Q.empty():
        c, m = Q.get()
        for i in range(n):
            for j in range(n):
                if i == j or G[c][m][i][j]:
                    continue
                # \/ ostatni warunek - żeby nie przeszli koło siebie jedną krawędzią
                if (M[c][i] or c == i) and (M[m][j] or m == j) and dist[i][j] >= d and (c, m) != (j, i):
                    G[c][m][i][j] = 1
                    Q.put((i, j))

    def DFS_visit(a, b):
        nonlocal visited, G, x, y, parent, n
        visited[a][b] = 1
        if visited[y][x]:
            return  # żeby niepotrzebnie nie robić dalej
        for i in range(n):
            for j in range(n):
                if G[a][b][i][j] == 1 and not visited[i][j]:
                    parent[i][j] = (a, b)
                    DFS_visit(i, j)

    visited = [[0 for _ in range(n)] for __ in range(n)]
    parent = [[None for _ in range(n)] for __ in range(n)]

    DFS_visit(x, y)

    path = [(y, x)]

    # odtwarzam rozwiązanie (zakładam że jest zgodnie z poleceniem)
    aux = (y, x)
    while parent[aux[0]][aux[1]] is not None:
        aux = parent[aux[0]][aux[1]]
        path.append(aux)
    path.reverse()

    return path


runtests(keep_distance)
