from zad3testy import runtests
from queue import PriorityQueue

# wrzucam do kolejki po kolei punkty odpowiadające za początki ikońce przedziałów, potem przeglądam je po kolei i
# sprawdzam długość przedziału i przedziaływchodzące w jego przecięcie
# tak to trzeba chyba zrobić ale gdzieś mam błąd i nie mogę go znaleźć



def kintersect(A, k):
    n = len(A)

    A = [(A[i], i) for i in range(n)]

    # sortuje po pierwszej współrzędnej
    A.sort(key=lambda x: x[0][0])

    def get_end(idx):
        nonlocal end_notsort, end, n
        for i in range(n):
            if end[idx] == end_notsort[i]:
                return i



    idxes = [A[i][1] for i in range(n)]
    beg = [A[i][0][0] for i in range(n)]
    end_notsort = [A[i][0][1] for i in range(n)]
    end = sorted(end_notsort)

    Q = []

    beg_idx = end_idx = 0

    for i in range(n):
        if beg_idx >= n:
            Q.append((end[end_idx], idxes[get_end(end_idx)], 'end'))
            end_idx += 1
        else:
            B, E = beg[beg_idx], end[end_idx]
            while B < E:
                Q.append((beg[beg_idx], idxes[beg_idx], 'beg'))
                beg_idx += 1
                if beg_idx == n:
                    break
                else:
                    B = beg[beg_idx]

            Q.append((end[end_idx], idxes[get_end(end_idx)], 'end'))
            end_idx += 1

    print()

    count = 0
    indexes = [0 for _ in range(n)]
    goal = []
    # start = Q[0][0]
    maxval = 0


    def find_start(idx):
        nonlocal A, n
        for i in range(n):
            if A[i][1] == idx:
                return A[i][0][0]

    def find_ending(idx):
        nonlocal A, n
        if idx is None:
            return float('inf')
        for i in range(n):
            if A[i][1] == idx:
                return A[i][0][1]

    for i in range(2*n):
        if Q[i][2] == 'beg':
            indexes[Q[i][1]] = 1
            count += 1
            start = Q[i][0]
        elif Q[i][2] == 'end':
            stop = Q[i][0]
            if count == k and maxval < stop - start:
                maxval = stop - start
                goal = [*indexes]
            indexes[Q[i][1]] = 0
            start = find_start(Q[i][1])
            count -= 1

    goal = [i for i in range(n) if goal[i]]

    return goal







runtests(kintersect)
