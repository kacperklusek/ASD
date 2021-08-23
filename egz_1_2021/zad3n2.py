from zad3testy import runtests


# O(n^2)


def kintersect(A, k):
    n = len(A)

    # zapisuje oryginalne indeksy przedziałów
    A = [[A[i], i] for i in range(n)]

    # sortuje po końcach przedziałów
    A.sort(key=lambda x: x[0][1])

    result_val = 0
    result = []
    for i in range(n):
        counter = 1
        tres = [A[i][1]]
        interval = A[i][0]
        for j in range(n-1, -1, -1):
            # rozne       obejmuje początek przedziału interval     i musze dołożyć przedział
            if i != j and A[j][0][0] <= A[i][0][0] < A[j][0][1] and counter < k:
                interval = (interval[0], min(interval[1], A[j][0][1]))
                tres.append(A[j][1])
                counter += 1
            if counter == k:
                tval = interval[1] - interval[0]
                if tval > result_val:
                    result_val = tval
                    result = tres
                break



    return result



runtests(kintersect)