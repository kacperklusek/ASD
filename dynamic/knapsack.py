def knapsack_nsumprofits(P, W, heavy_ass_weight):
    n = len(P)
    profits = 0
    mw = 0
    for i in range(n):
        profits += P[i]
        mw += W[i]

    F = [[None] * (profits + 1) for _ in range(n)]  # F[i][p] → najmniejsza waga elementów od 0 do i o sumie profitów równej p
    for i in range(n):
        F[i][0] = 0
    F[0][P[0]] = W[0]

    for i in range(1, n):
        for p in range(1, profits + 1):
            F[i][p] = F[i-1][p]     # zawsze mogę skipnąć dany element lub gdy mogę go wziąć, czyli da się dobrać do
            if P[i] <= p and F[i - 1][p - P[i]] is not None:                            # sumy profitów p, to go biore
                F[i][p] = W[i] + F[i - 1][p - P[i]] if F[i][p] is None or F[i][p] > W[i] + F[i - 1][p - P[i]] else F[i][p]

    output = 0
    for p in range(profits + 1):
        if F[n - 1][p] is not None and F[n - 1][p] <= heavy_ass_weight:
            output = p

    return output


# F[i] - najmniejsza waga o warości i

def knapsack_szprytny(P, W, heavy_ass_weight):
    n = len(P)
    max_profit = 0
    for i in range(n):
        max_profit += P[i]

    F = [None for _ in range(max_profit+1)]
    F[0] = 0

    for i in range(n):
        for p in range(max_profit-P[i], -1, -1):
            if F[p] is not None:
                F[p+P[i]] = min(F[p+P[i]], F[p]+W[i]) if F[p+P[i]] is not None else F[p] + W[i]

    for p in range(max_profit, -1, -1):
        if F[p] is not None and F[p] <= heavy_ass_weight:
            return p


def knapsack_nmaxw(P, W, maxw):
    n = len(W)
    F = [None] * n

    for i in range(n):
        F[i] = [0] * (maxw+1)
    for w in range(W[0], maxw+1):
        F[0][w] = P[0]

    for i in range(1, n):
        for w in range(1, maxw+1):
            F[i][w] = F[i-1][w]
            if w >= W[i]:
                F[i][w] = max(F[i][w], F[i-1][w-W[i]] + P[i])

    return F[n-1][maxw]


w = [4, 1, 2, 4, 3, 5, 10, 3]
p = [7, 3, 2, 10, 4, 1, 7, 2]
max_w = 10

P1 = [5, 8, 4, 5, 3, 7]
W1 = [4, 5, 12, 9, 1, 13]

print('res', knapsack_nmaxw(P1, W1, 25))
print('res', knapsack_nsumprofits(P1, W1, 25))
print('res', knapsack_nmaxw(P1, W1, 25))

print(knapsack_szprytny(p, w, max_w))
print(knapsack_nsumprofits(p, w, max_w))
print(knapsack_nmaxw(p, w, max_w))
