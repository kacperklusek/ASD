from zad1testy import runtests

def best_root( L ):
    n = len(L)
    visited = [0 for _ in range(n)]
    dist = [-1 for _ in range(n)]

    def DFS_visit(i, d=0):
        nonlocal visited, L, dist
        visited[i] = 1
        for j in L[i]:
            if not visited[j]:
                # print(f"visiting {j} from {i}") # zakomentować
                dist[j] = d + 1
                DFS_visit(j, d+1)

    first = second = 0

    # wyznaczam pierwszy z punktów najbardziej od siebie odległych
    DFS_visit(0)
    for i in range(n):
        if dist[first] < dist[i]:
            first = i

    # wyznaczam drugi z punktów najbardziej od siebie odległych
    visited = [0 for _ in range(n)]
    DFS_visit(first)
    for i in range(n):
        if dist[second] < dist[i]:
            second = i

    # wyznaczam środkowy punkt na drodze między first a second
    for i in range(n):
        if dist[i] == dist[second]//2:
            goal = i
            break

    return goal



runtests( best_root ) 
