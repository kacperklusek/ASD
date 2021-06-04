# F[i] - największy profit ze ścinania drzew od i do n-1, ścinając drzewo i


def forest(T):
    n = len(T)
    F = [0 for i in range(n)]
    F[n-1], F[n-2], F[n-3] = T[n-1], T[n-2], T[n-3] + T[n-1]

    for i in range(n-4, -1, -1):
        F[i] = max(T[i] + F[i+2], T[i] + F[i+3])

    to_cut = []
    s = m = 0 if F[0] > F[1] else 1
    while s < n-2:
        to_cut.append(T[s])
        if F[s] == F[s+2] + T[s]:
            s = s+2
        else:
            s = s+3

    if s < n:
        to_cut.append(T[s])

    return F[m], to_cut


t = [1, 3, 2, 5, 7, 8, 6, 3, 5, 1, 1, 2]
print(forest(t))
