def opt_sum(A):
    n = len(A)
    F = [[None for _ in range(n)] for __ in range(n)]

    for i in range(n):
        F[i][i] = (A[i], 0)

    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            if j - i == 1:
                F[i][j] = (A[i] + A[j], abs(A[i] + A[j]))
            else:
                wart = F[i][i][0] + F[i+1][j][0]
                op_sum = None
                for k in range(i, j):
                    if op_sum is None or max(F[i][k][1], F[k+1][j][1]) < op_sum:
                        op_sum = max(F[i][k][1], F[k+1][j][1], abs(wart))
                F[i][j] = (wart, op_sum)

    return max(abs(F[0][n-1][0]), F[0][n-1][1])


#########################################################

test_tabs = [[-999, -1000, 1001, 1000],
             [3, 2, -3, 4, 5, -9],
             [3, 6, 9, -8, -6, -3]]
test_costs = [998, 4, 5]


def runtests(f):
    OK = True
    for t, c in zip(test_tabs, test_costs):
        cost = f(t)
        print('Tablica: {0:30s}'.format(str(t)), end='')
        if cost == c:
            print('OK.      Największa wartosc bezwzgledna: ', str(cost))
        else:
            OK = False
            print('BLAD!    Największa wartosc bezwzgledna: {0:4d};'.format(cost), '   Powinno byc: ', str(c))
    print("----------------------------")
    if OK:
        print("OK!")
    else:
        print("Bledy!")


runtests(opt_sum)

