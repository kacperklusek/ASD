from zad3testy import runtests

    
def tasks(T):
    n = len(T)
    visited = [0 for _ in range(n)]
    output = []

    def DFS_visit(i):
        nonlocal visited, T, output
        visited[i] = 1
        for j in range(n):
            if T[i][j] == 1 and not visited[j]:
                DFS_visit(j)

        output.append(i)

    for i in range(n):
        if not visited[i]:
            DFS_visit(i)

    output.reverse()
    return output



runtests( tasks )
