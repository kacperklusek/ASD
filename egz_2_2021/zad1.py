from zad1testy import runtests

# dla każdego przedziału który zaczyna się w x, idę sposobem podobnym do algorytmu DFS jak po grafie.
# trzymam się zasady że mogę przeskoczyć z przedziału A na przedział B, gdy A[1] == B[0] czyli gdy maja 1 pkt wspólny
# zapisuje w tablicy czy da się dojść z danego weirzchołka do y, i korzystam z tego w późniejszych etapach programu,
# czyli jakbym chciał jeszcze raz wejść do danego wierzchołka

# O(n²)


def intuse( I, x, y ):
    n = len(I)
    solution = []

    visited = [0] * n
    can_reach = [False] * n

    def DFS_visit(i):
        nonlocal visited, I, can_reach
        visited[i] = 1
        if I[i][1] > y:
            return False
        elif I[i][1] == y:
            can_reach[i] = True
            return True

        can = False
        for j in range(n):
            if I[i][1] == I[j][0]:
                if not visited[j] and not can_reach[j]:
                    can = DFS_visit(j) or can
                elif visited[j] and can_reach[j]:
                    can = True

        can_reach[i] = can
        return can

    for i in range(n):
        if I[i][0] == x:
            DFS_visit(i)

    output = []
    for i in range(n):
        if can_reach[i]:
            output.append(i)

    return output

    
runtests( intuse )


