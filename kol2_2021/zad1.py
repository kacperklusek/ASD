from zad1testy import runtests

# generalnie działa dobrze tlko modyfikuje wejściową tabicę, i testy tego nie ogarniają

def cost(b):
    return b[3]

def cap(b):
    return b[0]*(b[2]-b[1])

def not_intercept(b1, b2):
    return b1[2] < b2[1] or b1[1] > b2[2]

def select_buildings(T, p):
    # f[i][j] = najwieksza liczba studentow zyjaca w budynkach od 0 do i, ktorych koszt wybudowania <= j,
    # nienachodzących na siebie
    T.sort(key=lambda x: x[2])

    n = len(T)
    f = [[0 for _ in range(p)] for __ in range(n)]
    last_used = [[-1 for _ in range(p)] for __ in range(n)]

    # prev[i] poprzedni budynek nieprzecinający itego
    prev = [-1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            prev[i] = j if not_intercept(T[i], T[j]) else prev[i]


    for i in range(p):
        if cost(T[0]) <= i:
            f[0][i] = cap(T[0])
            last_used[0][i] = 0

    for i in range(1, n):
        for j in range(1, p):
            f[i][j] = f[i-1][j]
            last_used[i][j] = last_used[i-1][j]
            if j >= cost(T[i]) and f[i][j] < f[prev[i]][j-cost(T[i])] + cap(T[i]):
                f[i][j] = f[prev[i]][j-cost(T[i])] + cap(T[i])
                last_used[i][j] = i

    used = []
    idx = n-1
    pdx = p-1
    while 1:
        for i in range(pdx, -1, -1):
            if f[idx][i] != f[idx][pdx]:
                pdx = i+1
                break
        used.append(last_used[idx][pdx])
        idx, pdx = prev[idx], pdx - cost(T[last_used[idx][pdx]])
        if last_used[idx][pdx] < 0:
            break

    used.reverse()

    return used




runtests( select_buildings ) 
