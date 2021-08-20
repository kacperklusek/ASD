from zad3testy import runtests

# O(n^3)

def intersect(inter1, inter2):
    if inter2[0] <= inter1[0] < inter2[1]:
        return min(inter2[1], inter1[1]) - inter1[0], (inter1[0], min(inter2[1], inter1[1]))
    if inter1[0] <= inter2[0] < inter1[1]:
        return min(inter1[1], inter2[1]) - inter2[0], (inter2[0], min(inter1[1], inter2[1]))
    else:
        return False

# inter1 contains inter2
def contains(inter1, inter2):
    if inter1[0] <= inter2[0] <= inter1[1] and inter1[0] <= inter2[1] <= inter1[1]:
        return True
    else:
        return False


def kintersect(A, k):
    n = len(A)

    if k == 1:
        result = 0
        resultid = 0
        for i in range(n):
            if A[i][1] - A[i][0] > result:
                result = A[i][1] - A[i][0]
                resultid = i
        return [resultid]

    if k == 2:
        result = 0
        resultid = []
        for i in range(n):
            for j in range(i+1, n):
                if intersect(A[i], A[j]):
                    tresult, tresultid = intersect(A[i], A[j])
                    if tresult > result:
                        result = tresult
                        resultid = tresultid
        return resultid

    fresult, fresultid = 0, []

    for i in range(n):
        for j in range(n):
            if intersect(A[i], A[j]) and i != j:
                count = 2
                result, interval = intersect(A[i], A[j])
                resultid = [i, j]
                for m in range(n):
                    if m == i or m == j:
                        continue
                    elif contains(A[m], interval):
                        count += 1
                        resultid.append(m)
                        if count == k:
                            if result > fresult:
                                fresult = result
                                fresultid = resultid
                            break

    return fresultid











runtests(kintersect)
