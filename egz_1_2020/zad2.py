from zad2testy import runtests




def opt_sum(tab):
    n = len(tab)
    # o[i][j] = najlepszy wynik dodajac elementy tablicy od i do j włącznie, (wart, abs(wart))
    o = [[None for _ in range(n)] for __ in range(n)]

    for i in range(n):
        o[i][i] = (tab[i], 0)

    for j in range(1, n):
        for i in range(j-1, -1, -1):
            if j-i == 1:
                o[i][j] = (tab[i] + tab[j], abs(tab[i] + tab[j]))
            else:
                val = o[i][i][0] + o[i+1][j][0]
                absval = None
                for k in range(i, j):
                    if absval is None or max(o[i][k][1], o[k+1][j][1]) < absval:
                        absval = max(o[i][k][1], o[k+1][j][1], abs(val))
                o[i][j] = (val, absval)

    return o[0][n-1][1]

runtests( opt_sum )
