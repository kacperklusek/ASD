# Kacper Kłusek
# sposób działania algorytmu:
# przede wszystkim sprawdzam, czy graf ma szansę być eulerowski, czyli sprawdzam WarunekKonieczny
# następnie z pomocą tablicy indexes, wykonuję algorytm DFS usuwając na bierząco krawędzie, po
# których przechodzę, oraz po przetworzeniu wierzchołka dodaję go na koniec tablicy result
# tym samym tworząc cykl eulera (wynikiem jest cykl eulera w odwrotnej kolejności niż na wykładzie
# ale nadal jest poprawny) do szukania sąsiadów danych wierzchołków korzystam z pomocy tablicy
# indexes, która mówi mi na którym sąsiedzie skończyłem ostatnim razem, oraz czy z danego wierz-
# chołka mogę jeszcze gdzieś przejść (czy ma jeszcze sąsiadów), tym samym unikając wielokrotnego
# sprawdzania istnienia tych samych krawędzi.
# 
# złożoność obliczeniowa mojego algorytmu to O(n²), ponieważ dla każdego wierzchołka sprawdzimy
# jego sąsiadów (każdego) dokładnie raz 


from copy import deepcopy


def restore(g, n):
    for i in range(n):
        for j in range(n):
            if g[i][j] == -1:
                g[i][j] = 1


def euler(G):
    n = len(G)
    result = []

    # sprawdzam warunek konieczny, bo w poleceniu zadania nie jest napisane, że graf jest eulerowski
    for i in range(n):
        s = 0
        for j in range(n):
            s += G[i][j]
        if s % 2:
            return None

    # ta tablica mówi mi odkąd zacząć szukać sąsiadów, oraz pozwala łatwo sprawdzić czy już
    # wszystkich sąsiadów wykorzystałem
    indexes = [0 for _ in range(n)]
    
    # ta tablica pozwala stwierdzić, czy wierzchołek został użyty w cyklu eulera (spójność)
    vertices = [False for _ in range(n)]

    def DFS(i=0):
        nonlocal G, n, result, indexes, vertices

        while indexes[i] < n:  # dopóki istnieje możliwość znalezienia sąsiada dla wierzchołka i
            neigh = indexes[i]
            if G[i][neigh] == 1:
                indexes[i] = neigh + 1              # odtąd zacznę szukać sąsiada, następnym razem
                G[i][neigh], G[neigh][i] = -1, -1     # usuwam krawędź
                DFS(neigh)
            else:                   # jak nie znalazłem sąsiada
                indexes[i] += 1     # to szukam dalej
        result.append(i)
        vertices[i] = True

    DFS()
    restore(G, n)   # przywracam graf do stanu początkowego

    # teraz sprawdzę czy graf jest spójny, sprawdzając czy result przechodzi przez każdy wierzchołek
    for i in range(n):
        if vertices[i] == False:    # gdy nie dodaliśmy tego wierzchołka do rozwiązania
            return None

    return result


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik


G = [[0, 1, 1, 0, 0, 0],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 0, 0, 1, 1],
     [0, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 1],
     [0, 1, 1, 1, 1, 0]]

GG = deepcopy(G)
cycle = euler(G)

if cycle == None:
    print("Błąd (1)!")
    exit(0)

u = cycle[0]
for v in cycle[1:]:
    if GG[u][v] == False:
        print("Błąd (2)!")
        exit(0)
    GG[u][v] = False
    GG[v][u] = False
    u = v

for i in range(len(GG)):
    for j in range(len(GG)):
        if GG[i][j] == True:
            print("Błąd (3)!")
            exit(0)

print("OK")
