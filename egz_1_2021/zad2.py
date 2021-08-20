from zad2testy import runtests
from queue import PriorityQueue


"""
algorytm wykorzystuje programowanie dynamiczne

d[v][o][x][y] - najkrótsza droga do pozycji (x, y) w grafie, z prędkością v i orientacją o

są 4 orientacje o
są 3 prędkości v
"""


def robot( L, A, B ):
    r = len(L)
    c = len(L[0])

    d = [[[[float('inf') for y in range(c)]
            for x in range(r)]
            for o in range(4)]
            for v in range(3)]

    # kierunki : prawo, dół, lewo, góra
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    speed = [60, 40, 30]


    Q = PriorityQueue()

    # wkładam do kolejki aktualną pozycje
    Q.put( [0, 0, 0, A[1], A[0]] )

    while not Q.empty():
        result, v, o, x, y = Q.get()

        # warunek końca
        if (y, x) == B:
            return result

        # sprawdzam, czy nie byłem już w tej sytuacji wcześniej, jak byłem to nie robie tego samego drugi raz
        if d[v][o][x][y] < float('inf'):
            continue
        else:
            d[v][o][x][y] = result

        # z aktualnej pozycji próbuje zrobić ruch do przodu (zwiekszając v) i obrócić się w lewo lub prawo (3 rzeczy)
        if L[x+dirs[o][0]][y+dirs[o][1]] != 'X':
            Q.put( [result + speed[v], min(v+1, 2), o, x+dirs[o][0], y+dirs[o][1]] )    # do przodu
        Q.put( [result + 45, 0, (o+1) % 4, x , y] ) # 90 w prawo
        Q.put( [result + 45, 0, (o+3) % 4, x , y] ) # 90 w lewo





runtests( robot )


