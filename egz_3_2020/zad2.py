from zad2testy import runtests

# w sumie po prostu LIS to jest n²

def tower(A):
    n = len(A)

    # h[i] = najwyższa wieża do klocka i
    h = [1 for i in range(n)]

    for i in range(1, n):
        for j in range(i):
            if A[i][0] >= A[j][0] and A[i][1] <= A[j][1]:
                # klocek i może leżeć na klocku j
                h[i] = max(h[i], h[j]+1)

    return max(h)




runtests( tower )
