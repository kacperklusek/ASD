from math import log2, ceil


def cat(x, y):
    t = []
    # zakładam że x i y są równej długości
    x.sort()
    y.sort()
    while x and y:
        if x[len(x)-1] < y[len(y)-1]:
            t.append(y.pop(len(y)-1))
        elif x[len(x)-1] > y[len(y)-1]:
            t.append(x.pop(len(x)-1))
        else:
            x.pop(len(x)-1)
            t.append(y.pop(len(y)-1))
        if len(t) > 1 and t[len(t)-1] == t[len(t)-2]:
            t.pop(len(t)-1)
    if x:
        t.extend(x[::-1])
    elif y:
        t.extend(y)

    return t


def parent(x):
    return (x-1)//2


def left(x):
    return 2*x + 1


def right(x):
    return 2*x + 2


def create_interval_tree(K):
    L, R = [interval[0] for interval in K], [interval[1] for interval in K]

    # intervals to przedziały bazowe
    intervals = cat(L, R)
    intervals.sort()
    intervals = [(intervals[i], intervals[i+1]) for i in range(len(intervals)-1)]

    # rozszerzam tablicę żeby była wielokrotnością dwójki
    target_len = 2 ** ceil( log2(len(intervals)) )
    while len(intervals) < target_len:
        intervals.append((float('inf'), float('inf')))

    # teraz dodaje na początek tablicy n-1 elementów, żebym mógł zrobić tablicową reprezentacje drzewa
    intervals = [None for _ in range(len(intervals)-1)] + intervals

    for i in range(len(intervals)-1, 2-1, -2):
        l, r = intervals[i-1][0], intervals[i][1]
        intervals[parent(i)] = (l, r)

    return intervals


K = [(1, 3, 1), (2, 5, 2), (0, 3, 2), (8, 9, 3), (4, 6, 1)]

inter_tree = create_interval_tree(K)

print(inter_tree)


# ##################################
# ##################################
# rozwiązanie tych spadających klocków o różnych wysokościach
# ##################################
#
# from math import log2, ceil
#
#
# def cat(x, y):
#     t = []
#     # zakładam że x i y są równej długości
#     x.sort()
#     y.sort()
#     while x and y:
#         if x[len(x)-1] < y[len(y)-1]:
#             t.append(y.pop(len(y)-1))
#         elif x[len(x)-1] > y[len(y)-1]:
#             t.append(x.pop(len(x)-1))
#         else:
#             x.pop(len(x)-1)
#             t.append(y.pop(len(y)-1))
#         if len(t) > 1 and t[len(t)-1] == t[len(t)-2]:
#             t.pop(len(t)-1)
#     if x:
#         t.extend(x[::-1])
#     elif y:
#         t.extend(y)
#
#     return t
#
#
# def parent(x):
#     return (x-1)//2
#
#
# def left(x):
#     return 2*x + 1
#
#
# def right(x):
#     return 2*x + 2
#
#
# def create_interval_tree(K):
#     L, R = [interval[0] for interval in K], [interval[1] for interval in K]
#
#     # intervals to przedziały bazowe
#     intervals = cat(L, R)
#     intervals.sort()
#     intervals = [(intervals[i], intervals[i+1]) for i in range(len(intervals)-1)]
#
#     # rozszerzam tablicę żeby była wielokrotnością dwójki
#     target_len = 2 ** ceil( log2(len(intervals)) )
#     while len(intervals) < target_len:
#         intervals.append((float('inf'), float('inf')))
#
#     # teraz dodaje na początek tablicy n-1 elementów, żebym mógł zrobić tablicową reprezentacje drzewa
#     intervals = [None for _ in range(len(intervals)-1)] + intervals
#
#     n = len(intervals)
#
#     for i in range(n-1, 2-1, -2):
#         l, r = intervals[i-1][0], intervals[i][1]
#         intervals[parent(i)] = (l, r)
#
#     # to dodałem, żeby przechowywać (przedział, maks. wysokość w obszarze węzła, czy jest liściem)
#     intervals = [[intervals[i],0, False] for i in range(n)]
#     intervals[0][2] = True
#
#     return intervals
#
#
# def intersects(x, y):
#     intersection = (max(x[0], y[0]), min(x[1], y[1]))
#     if intersection[0] < intersection[1]:
#         return intersection
#     else:
#         return False
#
#
# def put_block(L, R, h, T, i):
#     if T[i][0][0] == L and T[i][0][1] == R:
#         T[i][1] = h
#         T[i][2] = True
#     else:
#         ll, lr, rl, rr = T[left(i)][0][0], T[left(i)][0][1], T[right(i)][0][0], T[right(i)][0][1]
#         if ll <= L < R <= lr:
#             put_block(L, R, h, T, left(i))
#         elif rl <= L < R <= rr:
#             put_block(L, R, h, T, right(i))
#         else:
#             put_block(L, lr, h, T, left(i))
#             put_block(rl, R, h, T, right(i))
#
#         T[i][1] = max(T[i][1], h)
#         T[i][2] = False
#
#
# # zwraca poziom na jakim będziemy kłaść klocek
# def get_height(L, R, T, i):
#     if (T[i][0][0] == L and T[i][0][1] == R) or T[i][2]:
#         return T[i][1]
#     else:
#         ll, lr, rl, rr = T[left(i)][0][0], T[left(i)][0][1], T[right(i)][0][0], T[right(i)][0][1]
#         if ll <= L < R <= lr:
#             return get_height(L, R, T, left(i))
#         elif rl <= L < R <= rr:
#             return get_height(L, R, T, right(i))
#         else:
#             return max(get_height(L, lr, T, left(i)), get_height(rl, R, T, right(i)))
#
#
# def block_height(K):
#
#     T = create_interval_tree(K)
#
#     for l, r, h in K:
#         new_h = h + get_height(l, r, T, 0)
#         put_block(l, r, new_h, T, 0)
#
#     return T[0][1]
#
#
#
#
#
# K1 = [(1, 3, 1), (2, 5, 2), (0, 3, 2), (8, 9, 3), (4, 6, 1)]
# R1 = 5
#
# K2 = [(1, 3, 1), (2, 4, 1), (3, 5, 1), (4, 6, 1), (5, 7, 1), (6, 8, 1)]
# R2 = 6
#
# K3 = [(1, 10 ** 10, 1)]
# R3 = 1
#
# TESTY = [(K1, R1), (K2, R2), (K3, R3)]
#
# good = True
# for KK, RR in TESTY:
#     print("Klocki           : ", KK)
#     print("Oczekiwany wynik : ", RR)
#     WW = block_height(KK)
#     print("Otrzymany wynik  : ", WW)
#     if WW != RR:
#         print("Błąd!!!!")
#         good = False
#
# if good:
#     print("OK!")
# else:
#     print("Problemy!")