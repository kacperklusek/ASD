def check_prettiness(num):
    nums = [0 for i in range(10)]
    soles, multiples = 0, 0
    while num != 0:
        if nums[num % 10] == 0:  # liczba wystepuje raz to dodajemy do soles
            nums[num % 10] = 1
            soles += 1
        elif nums[num % 10] == 1:  # jak wystepuje kolejny raz to dodajemy do multiples i odejmujemy od soles
            nums[num % 10] = 2
            multiples += 1
            soles -= 1
        num //= 10
    return soles, multiples


def bucket_sort(t, v, key):
    n = len(t)
    buckets = [0] * v
    aux = t[:]  # pomocnicza tablica
    for i in range(n):
        buckets[aux[i][key]] += 1  ### key
    for i in range(1, v):
        buckets[i] += buckets[i - 1]
    for i in range(n - 1, -1, -1):
        buckets[aux[i][key]] -= 1  ### key
        t[buckets[aux[i][key]]] = aux[i]  ### key


def pretty_sort(t):
    n = len(t)
    for i in range(n):
        s, m = check_prettiness(t[i])  # t[n] = [123,   1145,   244,   5566,   5677]
        t[i] = s, m, t[i]  # t[n] = [(3,0,123), (2,1,1145), (1,1,244), (1,1,5566),  (2,1,5677)]

    bucket_sort(t, 10, 1)   # ręczny radix sort
    t.reverse()
    bucket_sort(t, 10, 0)
    t.reverse()


tab = [123, 1145, 244, 5566, 5677, 2256, 245, 21444, 21, 1]
pretty_sort(tab)
print(tab)
