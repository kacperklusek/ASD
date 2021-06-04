
def radix(t, key, start):   # stabilne
    n = len(t)
    chars = [[] for _ in range(26)]
    auxiliary_tab = [0 for _ in range(26)]

    for i in range(start, n):
        chars[ord(t[i][key]) - ord('a')].append(t[i])
        auxiliary_tab[ord(t[i][key]) - ord('a')] += 1

    c = 0
    for i in range(len(chars)):
        for j in range(len(chars[i])):
            t[start + c] = chars[i][j]
            c += 1


def sort_strings(t):    # t - lista stringów
    n = len(t)
    max_len = min_len = len(t[0])

    # znajduje największą i najmnniejszą długość stringa
    for i in range(n):
        if len(t[i]) > max_len:
            max_len = len(t[i])
        elif len(t[i]) < min_len:
            min_len = len(t[i])

    buckets = [[] for _ in range(max_len - min_len + 1)]  # n+1, bo zakładamy puste stringi
    len_counter = [0 for _ in range(max_len - min_len + 1)]

    # wrzucam stringi do odpowiednich kubełków względem ich długości    O(n)
    for i in range(n):
        buckets[len(t[i]) - min_len].append(t[i])
        len_counter[len(t[i]) - min_len] += 1

    for i in range(1, len(len_counter)):
        len_counter[i] += len_counter[i-1]

    c = 0
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            t[c] = buckets[i][j]
            c += 1

    # radix po odpowiednich indeksach:
    l_b = len(buckets)
    for i in range(l_b - 1, -1, -1):
        if len(buckets[i]) != 0:
            radix(t, min_len - 1 + i, len_counter[i] - len(buckets[i]))    # : tablica, indeks po ktorym sortujemy , indeks odkąd w tablicy

    if min_len > 1:
        for i in range(min_len - 2, -1, -1):
            radix(t, i, 0)


# t = ['aaa', 'aab', 'a', 'abba', 'aba', 'bac', 'baba', 'cab', 'cba', 'ccaaa', 'cc']
t = ['abecadlo', 'stefan', 'marian', 'ala', 'miasto', 'gory', 'zakopane', 'krakow', 'czlowiek', 'marmolada', 'aaaaaa', 'azaaaa', 'abecadloz']
sort_strings(t)
print(t)
# t = ['aaa', 'aab', 'a', 'abba', 'aba', 'bac', 'baba', 'cab', 'cba', 'ccaaa', 'cc']
t = ['abecadlo', 'stefan', 'marian', 'ala', 'miasto', 'gory', 'zakopane', 'krakow', 'czlowiek', 'marmolada', 'aaaaaa', 'azaaaa', 'abecadloz']
print(sorted(t))
