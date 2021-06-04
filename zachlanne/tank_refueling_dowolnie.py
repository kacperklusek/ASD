def go_tank(L, S, P, t):
    n = len(S)
    buy = [0 for _ in range(n)]

    next_best = 0
    for i in range(1, n):
        if S[i] <= L and P[i] < P[next_best]:
            next_best = i

    prev = next_best
    prev_range = L

    i = 1
    while i < n:
        p = S[prev]
        k = p + L
        next_best = i

        for j in range(i+1, n): # choosing the first best price in the buffor
            if S[j] > k:
                break
            elif P[j] <= P[next_best]:
                next_best = j
                while next_best+1 < n and S[next_best+1] <= k and P[next_best+1] == P[j]:
                    next_best += 1
                break

        if next_best == i and P[prev] < P[next_best] and S[prev]+L >= t:  # znaczy że nie ma żadnej tańszej stacji do końca
            buy[prev] = t - prev_range
            break

        i = next_best+1   # w następnej iteracji, będę zaczynał szukanie od następnej stacji niż teraźniejsza

        # jeśli kolejna najlepsza stacja ma tańsze paliwo to na poprzedniej powinienem zatankować tylko tyle, żeby
        # dojechać do tej lepszej i tankować na niej
        if prev != next_best and P[prev] >= P[next_best]:
            buy[prev] = S[next_best] - prev_range
            prev_range = S[next_best]
        # jak poprzednia była tańsza to znaczy że tankuje do pełna (potem dodtankuje troche na kolejnej najtańszej)
        elif prev != next_best and P[prev] < P[next_best]:
            buy[prev] = L - prev_range + S[prev]
            prev_range = S[prev] + L

        prev = next_best

        if next_best == n-1:    # jak mogę dotrzeć do końca z pola o najlepszej cenie to lece
            buy[next_best] = t - prev_range
            break

        if k > t:
            break

    price = sum(buy[i] * P[i] for i in range(n))
    print(buy)
    return price


# l = 10
# S = [8, 11, 15, 16]
# P = [40, 7, 15, 12]
# t = 23
# # wynik 134

l = 4
t = 14
S = [2, 4, 5, 6, 7, 9, 10, 11, 12, 13]
P = [4, 3, 2, 3, 3, 3, 3, 3, 3, 0.5]

# l = 14
# S = [1, 9, 15, 16, 17, 27, 28]
# P = [1, 100, 10, 15, 1, 30, 30]
# t = 30
# # Wynik u mnie: 34          1 + 20 + 13

print(go_tank(l, S, P, t))

