from random import randint, shuffle, seed

# działanie programu:
# za pomocą funkcji magicfives znajduję rekurencyjnie medianę median, tablicy
# następnie dzielę tablicę na elementy mniejsze i większe od mediany median za pomocą partition
# wywołuję rekurencyjnie funkcję linearselect z odpowiednią częścią tablicy, i odpowiednio modyfikując lub nie zmienną k
# oznaczającą indeks szukanej liczby


def partition(t, p, r, pivot):
    t[r], t[pivot] = t[pivot], t[r]
    last = p
    for i in range(p, r):
        if t[i] <= t[r]:
            t[i], t[last] = t[last], t[i]
            last += 1
    t[last], t[r] = t[r], t[last]
    return last


def insertion_sort(t, start, stop):
    for d in range(start, stop):
        for i in range(d, start - 1, -1):
            if t[i] > t[i + 1]:
                t[i + 1], t[i] = t[i], t[i + 1]
            else:
                break
    return t


def magicfives(A, start, stop):
    n = stop - start
    if n <= 1:
        return
    groups = (n + 4) // 5   # wyznaczam liczbę 'piątek'
    for i in range(groups):
        p, k = start + 5 * i, start + min(5 * i + 4, stop-1)     # p, k = początek i koniec każdej 'piątki'
        insertion_sort(A, p, k)                 # sortuje piątki żeby wyznaczyć medianę      (p+k)//2 to indeks mediany
        A[start + i], A[(p + k) // 2] = A[(p + k) // 2], A[start + i]       # wrzucam mediany piątek na początek listy
    magicfives(A, start, start + groups)   # rekurencyjnie wyznaczam medianę median


def linearselect(A, k, p=0, q=None):
    if q is None: q = len(A)
    if p == q:
        return A[p]

    magicfives(A, p, q)       # mediana median piątek zostaje wrzucona na pozycję 0
    piv = partition(A, p, q-1, p)     # dzielę tablice na elementy mniejsze i większe od mediany median, i ustawiam A[q]
                                    # na swoje miejsce
    if k < piv:                                   # <- przypadek gdy mediana median jest większa niż szukany element
        return linearselect(A, k, p, piv-1)            # wtedy szukamy w mniejszej od mediany części tablicy
    elif k == piv:                                # <- w tym przyapdku znaleźliśmy tę liczbę bo q jest na swoim miejscu w A
        return A[piv]
    else:                                       # < - przypadek gdy szukany element jest większy od mediany
        return linearselect(A, k, piv+1, q)      # wtedy szukamy w części większej od mediany, zmniejszając odpowiednio
                                                 # zmienna k, która będzie wtedy o q+1 mniejsza w tej części tablicy


seed(42)

n = 10
for i in range(n):
    A = list(range(n))
    shuffle(A)
    print(A)
    x = linearselect(A, i)
    if x != i:
        print("Blad podczas wyszukiwania liczby", i)
        exit(0)
print("OK")
