# Jakub Kosmydel
"""
Po znalezieniu indeksu (res_i) najkrótszej sciezki wywoluje funkcje, która to zapisuje w tablicy G
w która strone w miescie pod danym indeksem przebiegala sciezka (True/False - lewo/prawo). Nastepnie posiadajac
ta informacje prosto wypisuje ta tablice.
"""
from math import sqrt


def bitonicTSP(C):
    # Liczenie dystansu miedzy miastami c1 i c2
    def distance(c1, c2):
        return sqrt((c1[1] - c2[1]) ** 2 + (c1[2] - c2[2]) ** 2)

    n = len(C)
    # Sortuje podana tablice po wspolrzednych x, aby spelaniala warunki dla naszej rekurencji
    C.sort(key=lambda c: c[1])

    # Tablica przechowywujaca to co na wykladzie - dane z f(i, j)
    F = [[None] * n for _ in range(n)]

    # Tablica przechowujaca dystanse miedzy miastami: D[i][j] - dystans miedzy miastem i a j
    # Mógłbym te dane wyliczac za kazdym razem, wtedy bym zyskał na pamięci kosztem tego, że
    # niektóre obliczenia byłyby wielokrotnie powtarzane
    D = [[distance(C[i], C[j]) for j in range(n)] for i in range(n)]

    # Tablica przechowujaca "w którym kierunku" szlismy idac do miasta
    # pod danym indeksem - czy w prawo, czy w lewo
    G = [None] * n

    # Zapisuje dla pierwszych dwoch miast sciezke - to wzgledem nich bedziemy sie poruszac
    G[0] = True
    G[1] = False

    # Z wykladu: pierwsze 2 miasta (indeksy 0 i 1) musza byc polaczone, wpisuje odleglosc
    F[0][1] = D[0][1]

    def TSP(i, j, save=False):
        nonlocal F, C
        # Jezeli juz wyliczona jest ta wartosc to ja zwracamy
        if F[i][j] is not None:
            return F[i][j]
        if i == j - 1:
            # Szukam najoptymalniejszej sciezki, nastepnie zapisuje wynik do tablicy
            best = None
            for k in range(j - 1):
                new_d = TSP(k, j - 1, save) + D[k][j]
                if best is None or new_d < best:
                    best = new_d
            F[i][j] = best
        else:
            F[i][j] = TSP(i, j - 1, save) + D[j][j-1]
        return F[i][j]

    # Ta funkcja zapisuje do tablicy G w którym kierunku sciezka w danym miejsce przebiegala
    # (True/False - kierunki lewo/prawo), nastepnie dzieki temu mozemy prosto wypisac ta sciezke
    def find_solution(i, j):
        nonlocal G
        # Jezeli dla danego miasta juz ustalilismy kierunek sciezki to zwracamy
        if G[j] is not None:
            return G[j]
        if i == j - 1:
            # Wyszukuje z którym punktem sie lacze bezposrednio wczesniej
            best, best_i = None, None
            for k in range(j - 1):
                # Wyniki operacji TSP sa juz zapisane w tablicy, wiec nie wykonuje praktycznie zadnych nowych obliczen
                new_d = TSP(k, j - 1) + distance(C[k], C[j])
                if best is None or new_d < best:
                    best = new_d
                    best_i = k
            # Wyszukuje dla tego punktu jego kierunek sciezki, a nastepnie (poniewaz sa polaczone)
            # przepisuje ten kierunek dla obecnie rozpatrywanego punktu
            find_solution(best_i, j - 1)
            G[j] = G[best_i]
        else:
            # Jezeli jest to wczesniejszy punkt (i < j-1) to znajdujemy rekurencyjnie dla poprzedzajacego punktu
            # kierunek sciezki, i przepisujemy dla obecnie rozpatrywanego punktu
            find_solution(i, j-1)
            G[j] = G[j - 1]
        return G[j]

    # Znajduje rozwiazanie i indeks tego rozwiazania: (res_i, n-1)
    res, res_i = None, None
    for i in range(n - 1):
        val = TSP(i, n - 1) + distance(C[i], C[n - 1])
        if res is None or val < res:
            res, res_i = val, i
    dl = res
    # Posiadajac optymalne rozwiazanie szukam jego sciezki
    find_solution(res_i, n - 1)

    # Móglbym tutaj bezposrednio wypisywac oszczedzajac troszke pamieci,
    # jednak takie rozwiazanie uwazam za ladniejsze, a koszt pamieci niewielki.
    res = [C[0][0]]
    for i in range(n):
        if not G[i]:
            res.append(C[i][0])
    for i in range(n - 1, -1, -1):
        if G[i]:
            res.append(C[i][0])

    # Wypisuje rozwiazanie
    print(*res, sep=', ')
    print(dl)

# bitonicTSP([["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdańsk", 2, 4], ["Kraków", 3, 1]])


# # TESTY
#
# # C01: A F D B C E A
# C01 = [["A", 0, 2], ["B", 4, 3], ["C", 2, 4], ["D", 3, 1], ["E", 1, 3], ["F", 0.5, -2]]
#
# # C02: A I J H D E G F C B A
# C02 = [['A', 0, 2], ['B', 1, 1], ['C', 4, 1], ['D', 5, 3], ['E', 6, 3], ['F', 8, 3], ['G', 7, 4], ['H', 2, 4],
#        ['I', 0.5, 2.5], ['J', 1.5, 3.5]]
#
# # 1 2 3 4 5 6 7 8 9 10 1
# C03 = [["1", 0, 1], ["2", 1, -6], ["3", 3, -1], ["4", 6, -2], ["5", 10, 1], ["6", 14, 3], ["7", 9, 4], ["8", 7, 2], ["9", 4, 3], ["10", 2, 3]]
#
# # C10: A, B, C, E, F, D, A
# C10 = [['A', 0, 2], ['B', 1, 4], ['C', 3, 5], ['D', 4, 1], ['E', 5, 5], ['F', 6, 4], ['G', 2, 1]]
#
# # C1: Wrocław, Kraków, Warszawa, Gdańsk, Wrocław
# C1 = [["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdańsk", 2, 4], ["Kraków", 3, 1]]
#
# tests = [("A, B, C, E, F, D, G, A", C10),
#          ("A, F, D, B, C, E, A", C01),
#          ("A, I, J, H, D, E, G, F, C, B, A", C02),
#          ("1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1", C03),
#          ("Wrocław, Kraków, Warszawa, Gdańsk, Wrocław", C1)]
#
# for test in tests:
#     print('CORRECT:', test[0])
#     print(' ANSWER: ', end='')
#     bitonicTSP(test[1])
#     print('---')


C = [('A', 2, -11), ('B', 11, -8), ('C', 20, 38), ('D', 42, -42), ('E', 65, -22), ('F', 66, 23), ('G', 67, -73), ('H', 84, 50), ('I', 94, -92), ('J', 99, 74)]
bitonicTSP(C)
