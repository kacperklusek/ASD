from zad3testy import runtests
from math import ceil, log2


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
        for i in range(len(x)):
            if x[i] != t[len(t) - 1]:
                t.append(x[i])
    elif y:
        for i in range(len(y)):
            if y[i] != t[len(t) - 1]:
                t.append(y[i])

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
    intervals = [(intervals[i]+1, intervals[i+1]) for i in range(len(intervals)-1)]

    # rozszerzam tablicę żeby była wielokrotnością dwójki
    target_len = 2 ** ceil( log2(len(intervals)) )
    while len(intervals) < target_len:
        intervals.append((float('inf'), float('inf')))

    # teraz dodaje na początek tablicy n-1 elementów, żebym mógł zrobić tablicową reprezentacje drzewa
    intervals = [None for _ in range(len(intervals)-1)] + intervals

    n = len(intervals)

    # uzupełniam parentów
    for i in range(n-1, 2-1, -2):
        l, r = intervals[i-1][0], intervals[i][1]
        intervals[parent(i)] = (l, r)

    # to dodałem, żeby przechowywać (przedział, kolor)
    intervals = [[intervals[i], 0] for i in range(n)]

    return intervals


def put_block(L, R, T, i):
    if not (T[i][0][0] <= L < T[i][0][1] or T[i][0][0] < R <= T[i][0][1] or L <= T[i][0][0] <= T[i][0][1] <=R):
        return 0
    else:
        if i >= len(T)//2:
            T[i][1] += 1
            T[i][1] %= 3
            return T[i][0][1] - T[i][0][0] if T[i][1] == 2 else -T[i][0][1] + T[i][0][0] if T[i][1] == 0 else 0

    # ll, lr, rl, rr = T[left(i)][0][0], T[left(i)][0][1], T[right(i)][0][0], T[right(i)][0][1]
    return put_block(L, R, T, left(i)) + put_block(L, R, T, right(i))


def lamps( n,T ):
    l = create_interval_tree(T)

    result = 0
    counter = 0

    for left, right in T:
        counter += put_block(left, right, l, 0)

        result = max(result, counter)

    return result


runtests( lamps )
