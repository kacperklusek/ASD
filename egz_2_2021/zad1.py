from zad1testy import runtests

# dla każdego przedziału który zaczyna się w x, idę sposobem podobnym do algorytmu DFS jak po grafie.
# trzymam się zasady że mogę przeskoczyć z przedziału A na przedział B, gdy A[1] == B[0] czyli gdy maja 1 pkt wspólny
# zapisuje po drodze przedziały z jakich korzystałem i jeśli dojde do takiego, którego prawy koniec jest równy y, to
# znaczy że znalazłem jedno z rozwiązań, zapisuje je więc pomijając powtórki do zmiennej solution i kontynuuje
# złożoność algorytmu to złożoność dfs czyli O(n²)

# na moim komputerze testy zacinają się na teście 4, ale algorytm wydaje siębyć poprawny

def intuse( I, x, y ):
    n = len(I)
    solution = []

    I = [[I[i][0], I[i][1], i] for i in range(n)]

    # sortuje po zerowych indeksach
    I.sort(key=lambda x:x[0])

    def dfs(i, temp_solution):
        nonlocal solution, I, x, y, n
        if I[i][1] == y:
            for idx in temp_solution:
                if idx not in solution:
                    solution.append(idx)
            return
        elif I[i][1] < y:
            for j in range(0 if i == n else i, n):
                if I[j][0] > I[i][1]:
                    break
                # jeśli rozważam różne przedziały && da się przeskoczyć na drugi && drugi nie wykracza poza przedział x, y
                if i != j and I[j][0] == I[i][1] and I[j][1] <= y:
                    dfs(j, temp_solution + [I[j][2]])

    # tworzę sztuczny wierzchołek (przedział) który jest początkiem rozwiązań.
    # nie wlicza się on do rozwiązania
    I.append([float('inf'), x, n])
    dfs(n, [])

    return solution

    
runtests( intuse )


