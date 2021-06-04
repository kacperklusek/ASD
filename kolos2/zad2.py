from zad2testy import runtests
from collections import deque

# działanie algorytmu:
# zamieniam reprezentacje grafu z listowej na macierzową O(n²)
# dwa razy wykonuję algorytm BFS na podanym grafie, raz żeby znaleźć najkrótszą ścieżkę, a drugi raz, żeby sprawdzić,
# czy któraś z krawędzi tej ścieżki leży na cyklu, bo wtedy wystarzy usunąć tę krawędź, i wtedy najkrótsza ścieżka
# będzie przechodziła przez ten cykl, czyli będzie conajmniej o 1 dłuższa lub będzie inną dłuższą ścieżką nieprzechodzą-
# cą przez ten cykl O(n²)
# sprawdzam też po drodze czy ścieżka istnieje, i czy do docelowego wierzchołka dochodzą dwie ścieżki o takiej samej
# długości, wtedy jak usuniemy coś na jednej ścieżce, to nadal będzie można dojść tą drugą
# złożoność onliczeniowa algorytmu to O(n²)


def switch_repres(G):
    n = len(G)
    G_matrix = [[0 for _ in range(n)] for __ in range(n)]
    for i in range(n):
        for ind in G[i]:
            G_matrix[i][ind] = 1
            G_matrix[ind][i] = 1

    return G_matrix


def enlarge(G, s, t):

    G = switch_repres(G)

    n = len(G)
    queue = deque([s])
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    visited[s] = True
    d = [-1 for _ in range(n)]
    d[s] = 0
    checking = False
    found = False
    path = []

    def BFS_visit(i):
        nonlocal G, queue, parent, visited, d, checking, result_edge, found

        for j in range(n):
            if G[i][j] == 1 and not visited[j]:
                parent[j] = i
                d[j] = d[i] + 1  # d[i] == d[parent[j]]
                queue.appendleft(j)
                visited[j] = True

            if G[i][j] == 1 and j == t:
                found = True

            if checking:        # tylko dladrugiego wykonania BFS
                if G[i][j] == 1 and visited[j] and d[j] > 0 and path[d[j]] == j and i != path[d[j] - 1]:
                    checking = False
                    result_edge = (parent[j], j)
                    return



    while len(queue) > 0:
        BFS_visit(queue.pop())

    if not found:
        return None
    else:
        count = 0
        for i in range(n):
            if G[t][i] == 1 and d[i] == d[t] - 1:
                count += 1
            if count == 2:
                return None

    x = t
    while x != s:
        path.append(x)
        x = parent[x]

    path.append(s)
    path.reverse()

    # drugie wykonanie BFS
    visited = [False for _ in range(n)]     #
    visited[s] = True                       # resetuje tablice pomocnicze

    queue = deque([s])
    checking = True
    result_edge = None
    while len(queue) > 0 and checking:
        BFS_visit(queue.pop())

    return result_edge



runtests( enlarge )

#
#
#
#
#
#
# from zad2testy import runtests
# from collections import deque
#
# # działanie algorytmu:
# # zamieniam reprezentacje grafu z listowej na macierzową O(n²)
# # dwa razy wykonuję algorytm BFS na podanym grafie, raz żeby znaleźć najkrótszą ścieżkę, a drugi raz, żeby sprawdzić,
# # czy któraś z krawędzi tej ścieżki leży na cyklu, bo wtedy wystarzy usunąć tę krawędź, i wtedy najkrótsza ścieżka
# # będzie przechodziła przez ten cykl, czyli będzie conajmniej o 1 dłuższa lub będzie inną dłuższą ścieżką nieprzechodzą-
# # cą przez ten cykl O(n²)
# # sprawdzam też po drodze czy ścieżka istnieje, i czy do docelowego wierzchołka dochodzą dwie ścieżki o takiej samej
# # długości, wtedy jak usuniemy coś na jednej ścieżce, to nadal będzie można dojść tą drugą
# # złożoność onliczeniowa algorytmu to O(n²)
#
#
# # sprawdzam dla kazdego wierzchołka z path, czy ma max jednego sąsiada o 'd' równym d wierzchołka - 1
# # oraz czy ma jakiegoś sąsiada o d równym bąddź wiekszym swojemu, wtedy istnieje taka krawędź którą jeka usuniemu to
# # droga z s do t będzie dłuższa
#
#
#
# def switch_repres(G):
#     n = len(G)
#     G_matrix = [[0 for _ in range(n)] for __ in range(n)]
#     for i in range(n):
#         for ind in G[i]:
#             G_matrix[i][ind] = 1
#             G_matrix[ind][i] = 1
#
#     return G_matrix
#
#
# def enlarge(G, s, t):
#
#     G = switch_repres(G)
#
#     n = len(G)
#     queue = deque([s])
#     parent = [None for _ in range(n)]
#     visited = [False for _ in range(n)]
#     visited[s] = True
#     d = [-1 for _ in range(n)]
#     d[s] = 0
#     checking = False
#     found = False
#     path = []
#
#     def BFS_visit(i):
#         # nonlocal G, queue, parent, visited, d, checking, result_edge, found
#         nonlocal G, queue, parent, visited, d, checking, found
#
#         for j in range(n):
#             if G[i][j] == 1 and not visited[j]:
#                 parent[j] = i
#                 d[j] = d[i] + 1  # d[i] == d[parent[j]]
#                 queue.appendleft(j)
#                 visited[j] = True
#
#             if G[i][j] == 1 and j == t:
#                 found = True
#
#             # if checking:        # tylko dladrugiego wykonania BFS
#             #     if G[i][j] == 1 and visited[j] and d[j] > 0 and path[d[j]] == j and i != path[d[j] - 1]:
#             #         checking = False
#             #         result_edge = (parent[j], j)
#             #         return
#
#
#
#     while len(queue) > 0:
#         BFS_visit(queue.pop())
#
#     if not found:
#         return None
#
#
#     x = t
#     while x != s:           # buduję ścieżkę
#         path.append(x)
#         x = parent[x]
#
#     path.append(s)
#     path.reverse()
#
#
#     found = False
#     edge = ()
#     for p in range(0, len(path)):
#         count = 0
#         bigger_dist = False
#         for i in range(n):
#             if G[path[p]][i] == 1 and d[i] == d[path[p-1]]:
#                 count += 1
#             if count > 1:
#                 break
#             #  istnieje krawedz          o odl >= od swojej       która nie nalezy do ścieżki
#             if G[path[p]][i] == 1 and d[i] >= d[path[p]] and p+1 < len(path) and i != path[p+1]:
#                 bigger_dist = True
#                 edge = (path[p], path[p+1])
#                 break
#
#         if count == 1 and bigger_dist:
#             return edge
#
#     return None
#     # # drugie wykonanie BFS
#     # visited = [False for _ in range(n)]     #
#     # visited[s] = True                       # resetuje tablice pomocnicze
#     #
#     # queue = deque([s])
#     # checking = True
#     # result_edge = None
#     # while len(queue) > 0 and checking:
#     #     BFS_visit(queue.pop())
#     #
#     # return result_edge
#
#
#
# runtests( enlarge )
#
