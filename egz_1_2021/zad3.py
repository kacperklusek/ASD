from zad3testy import runtests
from queue import PriorityQueue


# O(n^2)


def kintersect(A, k):
    n = len(A)

    # przygotowuje tablice punktów
    A_p = [(l, r, idx) for idx, (l, r) in enumerate(A)]

    L = [(l, idx, 0) for l, r, idx in A_p]
    R = [(r, idx, 1) for l, r, idx in A_p]

    points = L + R
    points.sort()

    # info o aktywnych przedziałach
    intervals_used = []     # <- aktualnie używane przedziały
    active = 0              # <- liczba aktualnie używanych przedziałów
    q = PriorityQueue()     # <- kolejka końców aktualnie używanych przedziałów, przechowuje (end_point, idx)
                            #    gdzie idx to indeks przedziału w A
    # info o wynikach
    best = [None, None]

    # teraz będę iterował po punktach
    for v, idx, end in points:

        # jeśli napotkam początek, to wrzucam do PQ jego koniec i zwiększam liczbe aktywnych przedziałów
        if end == 0:
            active += 1
            intervals_used.append(idx)
            q.put((A[idx][1], idx))
        # jeśli spotkam koniec to wyrzucam go z PQ i zmniejszam liczbe aktywnych przedziałów
        elif end == 1:
            # trzeba sprawdzić czy jest, bo mógł się usunąć w linii 51
            if idx in intervals_used:
                active -= 1
                intervals_used.remove(idx)  # <- działa w O(k)
                q.get()

        # jeśli liczba aktywnych przedziałów jest większa od k, to należy usunąć najgorszy przedział
        # tzn. taki który kończy się najwcześniej, bo najlepsze przecięcie k przedz. z jego udziałem już sprawdziliśmy
        while active > k:
            # linia 38
            if idx in intervals_used:
                active -= 1
                ending, idx = q.get()
                intervals_used.remove(idx)

        # jeśli liczba aktywnych przedziałów jest równa k, to muszę znaleźć maksimum z początków aktywnych przedziałów
        # oraz minimum z końców aktywnych przedziałów
        if active == k:
            # min z końców:
            ending, idx = q.get()
            q.put((ending, idx))
            # max z początków:
            beginning = float('-inf')
            for i in intervals_used:
                beginning = max(beginning, A[i][0])

            # poprawiam najlepszy wynik
            temp = ending - beginning
            if best[0] is None or best[0] < temp:
                best[0] = temp
                best[1] = intervals_used[:]

    return best[1]


runtests(kintersect)
