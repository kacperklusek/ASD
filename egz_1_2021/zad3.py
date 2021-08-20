from zad3testy import runtests


# O(n^2)

def kintersect(A, k):
    n = len(A)

    # zapisuje oryginalne indeksy przedziałów
    A = [(A[i], i) for i in range(n)]

    # sortuje po końcach przedziałów
    A.sort(key=lambda x: x[0][1])


    result_val = 0
    for i in range(n):
        result = []
        






runtests(kintersect)