# KACPER KŁUSEK
# Działanie algorytmu:
# Na początku wyznaczam sobie długość najkrótszej ścieżki wypełniając przy tym tablicę F oraz D
# F[i][j] = najmniejsza suma długości ścieżek od miasta o indeksie 0 do j i od miasta od ind. i do 0
# D[i][j] = D[j][i] = odległosć miast o ideksach i oraz j
# do wyznaczenia najkrótszej ścieżki bitonicznej przechodzącej po wszystkich miastach używam funkcji z wykładu
# natomiast do odtworzenia ścieżki:
# · wybieram najkrótszą ze ścieżek F[idx][n-1] znajdując 'idx', który oznacza indeks pierwszego od prawej elementu
#   w ścieżce powrotnej (nie licząc elementu od ind. n-1)
# · do listy 'path' wypełnionej zerami wpisuje jedynki, pod te indeksy, które odpowiadają miastom w drodze powrotnej;
# · na końcu wypisuje wynik
#
# złożoność obliczeniowa funkcji wyznaczającej długość najkrótszej ścieżi to O(n²) a funkcji zwracającej 'path'
# też O(n²), samo wypisanie wyniku to O(n), zatem cały algorytm ma złożoność O(n²)
from math import *


# zwraca tablicę zer i jedynek, gdzie 1 oznacza miasto w drodze powrotnej a 0 w drodze w prawo
def get_path(F, D, ind):
    n = len(F)
    path = [0 for _ in range(n)]

    def fill_path(idx, prev):  # najgorszy przypadek ma złożoność O(n²), prev to następny element na 'drugiej' ścieżce
        nonlocal F, D, path
        if idx < 1:
            return

        path[idx] = 1

        s = 0
        mnm = F[0][idx] + D[0][prev]
        for k in range(1, idx):  # O(n); znajduje indeks s oznaczający ostatni przed idx element na 'drugiej' ścieżce
            if F[k][idx] + D[k][prev] <= mnm:
                mnm = F[k][idx] + D[k][prev]
                s = k

        for i in range(s + 1, idx):
            path[i] = 1

        if s == 0:
            return

        s1 = 0
        mnm = F[0][s] + D[0][s + 1]
        for k in range(1,
                       s):  # O(n); znajduje indeks s1 oznaczający ostatni przed s indeks na 'drugiej' czyli bazowej ścieżce
            p = mnm
            mnm = min(mnm, F[k][s] + D[k][s + 1])
            s1 = k if p != mnm else s1

        fill_path(s1, s1 + 1)  # maksymalnie O(n) razy

    fill_path(ind, ind + 1)  # O(n²)

    return path


def d(i, j, tab, D):  # odległośći
    if D[j][i] > 0:
        return D[j][i]
    else:
        return sqrt((tab[i][2] - tab[j][2]) ** 2 + (tab[i][1] - tab[j][1]) ** 2)


def bitonicTSP(C):
    def TSP(i, j):
        nonlocal F, D
        if F[i][j] is not None:
            return F[i][j]
        if i == j - 1:
            mnm = TSP(0, i) + D[0][j]
            for k in range(1, j - 1):
                mnm = min(mnm, TSP(k, j - 1) + D[k][j])
            F[i][j] = mnm
        else:
            F[i][j] = TSP(i, j - 1) + D[j - 1][j]

        return F[i][j]

    n = len(C)
    C.sort(key=lambda x: x[1])

    D = [[-1 for _ in range(n)] for __ in range(n)]  # zapisuję tablicę odległośći
    for i in range(n):
        for j in range(n):
            D[i][j] = d(i, j, C, D)

    F = [[None for _ in range(n)] for __ in range(n)]  # przygotowuję tablicę F

    F[0][1] = D[0][1]  # warunek początkowy

    # m_idx to indeks pod którym jest pierwsze od prawej miasto na ścieżce powrotnej
    m = TSP(0, n - 1) + D[0][n - 1]
    m_idx = 0
    for i in range(1, n - 1):
        if TSP(i, n - 1) + D[i][n - 1] < m:
            m_idx = i
            m = TSP(i, n - 1) + D[i][n - 1]

    path = get_path(F, D, m_idx)

    # printowanie wyniku:
    for i in range(n):
        if path[i] == 0:
            print(C[i][0], end=', ')

    for i in range(n - 1, -1, -1):
        if path[i]:
            print(C[i][0], end=', ')

    print(C[0][0])
    print(m)
