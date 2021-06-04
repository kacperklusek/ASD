from time import time


# Działanie programu:
# funkcja printAllLIS działa tak jak podana na wykładzie funkcja szukająca LIS danej tablicy, z tym wyjątkiem, że
# tworzy ona tablicę tablic wszystkich rodziców każdej liczby, żeby można było później ich szybko odnaleźć
# do stworzenia tablicy P (parents), trzeba użyć algorytmu szukającego LIS o złożoności n^2, bo chcemy znać wszystkich
# możliwych rodziców dla danego indeksu
# następnie wywołuję funkcję printsolution, która ma zadanie wypisać wszystkie LIS-y, i robi to w następujący sposób:
#   znajduje po kolei wszystkie elementy które są końcami LIS-a, i dla każdego tego elementu będzie budowało listę,
#   która będzie reprezentacją tego podciągu, rekurencyjnie wypełniam tablicę kolejnymi rodzicami, aż dojdę wapełnię
#   tablicę do końca (pokaże mi to zmienna fill, gdy fill == 0). Gdy tablica jest pełna, wypisuje ją i zwiększam
#   licznik 'count' o 1.
#
# kończę program zwracając zmienną count, przechowującą w sobie informację na temat liczby LIS'ów
#
# Złożoność obliczeniowa programu to O(n^2) ze względu na znajdowanie LIS'ów (bez ich wypisywania),
# aby oszacować złożoność czasową printsoultion, rozważmy ciąg liczb długości n, oraz najdłuższy rosnący podciąg (LIS) o
# długości k, wtedy liczba wszystkich LIS'ów jest ograniczona od góry przez n^(n/k)
# funkcja f(x)=x^(n/x) przyjmuje maksimum dla x=e
# zatem największa złożoność czasowa to e^(n/e) = O(e^n)



def printsolution(A, F, P, m):
    count = 0

    def printLIS(A, P, i, result, fill):
        nonlocal count
        for j in range(len(P[i])):
            result[fill] = A[i]
            if fill == 0:
                print(*result, sep=' ')
                count += 1
            else:
                printLIS(A, P, P[i][j], result, fill - 1)

    n = len(A)
    for i in range(n):
        if F[i] == m:
            result = [0 for i in range(m)]
            printLIS(A, P, i, result, m - 1)

    return count


def printAllLIS(A):
    n = len(A)
    F = [1 for _ in range(n)]
    F[0] = 1
    P = [[-1] for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i] and F[i] <= F[j] + 1:
                if F[i] != F[j] + 1:
                    P[i] = [j]
                    F[i] = F[j] + 1
                else:
                    P[i].append(j)

    lngst = max(F)
    count = printsolution(A, F, P, lngst)

    return count

# ---------------------------------------

def lis(T):
    # funkcja szukająca "mapy" pozwalającej odtworzyć szukane najdłuższe podciągi rosnące
    n = len(T)
    longest = [1] * n

    # coś w rodzaju kolejki pełzającej z szukaną "mapą"
    children = [[[None] * n, -1, -1] for _ in range(n)]

    # szukamy najdłuższych ciągów malejących w odwróconej tablicy
    for i in range(n - 1, -1, -1):
        # przechodzimy od dołu do góry, aby mieć "mapę" w odpowiedniej kolejności
        for j in range(i + 1, n):
            if T[j] > T[i] and longest[j] + 1 >= longest[i]:
                # przesuwamy "kolejkę", bo znaleźliśmy dłuższy podciąg
                if longest[j] + 1 > longest[i]:
                    longest[i] = longest[j] + 1
                    children[i][1] = children[i][2] = children[i][2] + 1
                # dodajemy nowe rozgałęzienie "mapy"
                children[i][0][children[i][2]] = j
                children[i][2] += 1

    # zwracamy długość najdłuższego podciągu, tablicę z początkami najdłuższych podciągów i "mapę" mówiącą jak dostać wyniki
    return max(longest), longest, children


def printAllLISb(T):
    # licznik
    cnt = 0

    def get_solution(T, children, seq, ind, i):
        nonlocal cnt
        if ind == 1:
            # dotarliśmy do ostatniego elementu podciągu i możemy go wypisać
            seq[len(seq) - ind] = T[i]
            for i in range(len(seq)):
                print(seq[i], end=" ")
            print()
            cnt += 1
            return

        # dopisujemy element do podciągu wynikowego
        seq[len(seq) - ind] = T[i]
        # przechodzimy do następnego elementu podciągu
        for j in range(children[i][1], children[i][2]):
            get_solution(T, children, seq, ind - 1, children[i][0][j])

    # uzyskujemy informacje o podciągach i "mapę" do ich wypisania
    res, longest, children = lis(T)
    # tu będziemy budować podciągi
    seq = [-1] * res
    for ind in range(len(T)):
        # szukamy początku i rozpoczynamy budowę podciągów
        if longest[ind] == res:
            get_solution(T, children, seq, res, ind)

    # zwracamy licznik
    return cnt


# ------ testy ------
# A = [13, 7, 21, 42, 8, 2, 44, 53]
A = [10 * k + i for k in range(8) for i in range(6, 0, -1)]

start = time()
print(printAllLIS(A))
stop = time()

startb = time()
print(printAllLISb(A))
stopb = time()

print('kacper', stop - start)
print('bartek', stopb - startb)
