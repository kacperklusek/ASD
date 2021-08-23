from zad3testy import runtests
from queue import PriorityQueue


# Sortujemy leksykograficznie, teraz utrzymujemy zawsze k-najlepszych przedzialow (najdalej sie konczacych i aktywnych) by zebrac najlepszy.
# kazdy przedzial zostatnie dokladnie raz dodany i odjety z kolejki priorytetowej
# stad zlozonosc O(n*logk), ale wyszukujemy jeszcze naiwnie minimum stad O(n*k)

def kintersect(A, k):
    A_p = [(l, r, idx) for idx, (l, r) in enumerate(A)]
    A_p.sort()

    L = [(l, idx, 0) for (l, r, idx) in A_p]
    R = [(r, idx, 1) for (l, r, idx) in A_p]

    points = sorted(L + R)

    ans = list(range(k))
    ans_v = 0

    active_intervals = []

    q = PriorityQueue()

    # print('Points', points)
    for (v, idx, b) in points:

        # print("1.",active_intervals)

        if b == 0:
            active_intervals.append(idx)
            q.put((A[idx][1], idx))
        if b == 1:
            if idx in active_intervals:
                active_intervals.remove(idx)

        while len(active_intervals) > k:
            # print("USUWAMY:",v, idx)
            v, idx = q.get()
            if idx in active_intervals:
                active_intervals.remove(idx)

        # print("2.",active_intervals)
        if len(active_intervals) == k:
            min_R, idx = q.get()
            q.put((min_R, idx))
            L = [A[i][0] for i in active_intervals]
            cand = min_R - max(L)
            if cand > ans_v:
                ans_v = cand
                ans = active_intervals.copy()
        # print("3.",active_intervals)

    return ans


runtests(kintersect)
