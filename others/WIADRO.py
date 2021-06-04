'''Mamy serię pojemników z wodą, połączonych (każdy z każdym) rurami.Pojemniki maja kształty prostokątów,
rury nie maja objetosci (powierzchni). Każdy pojemnik opisany jest przez współrzędne lewego górnego rogu
i prawego dolnego rogu. Wiemy, ze do pojemników nalano A “powierzchni” wody (oczywiście woda rurami spłynęła
do najniższych pojemników). Proszę zaproponować algorytm Obliczający ile pojemników zostało w pełni zalanyc'''

containers = [[(1, 3), (2, 1)], [(2, 5), (3, 4)], [(3, 6), (4, 3)], [(4, 8), (5, 7)], [(5, 10), (6, 5)]]


def try_to_fill(L, n, c):
    count = 0
    for coords in c:
        bott = coords[1][1]
        ceil = coords[0][1]
        width = coords[1][0]-coords[0][0]
        L -= max(0, width*(n - bott)) if n <= ceil else width*(ceil - bott)
        if ceil <= n:
            count += 1
        if L < 0:
            break

    return L >= 0, count


def fill(L, c):
    top = 0
    for coord in c:
        if coord[0][1] > top:
            top = coord[0][1]

    max_count = 0
    bottom = 0

    while top >= bottom:
        idx = (top + bottom)//2
        possible, count = try_to_fill(L, idx, c)
        if possible:
            max_count = count
            bottom = idx + 1
        else:
            top = idx - 1

    return max_count


print(fill(10, containers))
