# Kacper Kłusek
# działanie programu:
#  najpierw tworzę tablicę T, która składa się z posortowanych względem litery obiektów klasy Node i przechowuje
#  "ostatnie, najniżej położone" liście drzewa którego będę używał do odtwarzania kodów, następnie tworzę drzewo,
#  wybierając z kolejki prioretytowej dwa najrzadziej występujące elementy (l oraz r), tworzę nowy Node,
#  o wartości sumy częstości dwóch wybranych elementów, ustawiam nowy None jako rodzic l i r, i wstawiam go do kolejki
#  złożoność powyższej części to O(nlogn)
#
# wypisywanie wyniku:
#  do wypisywania wyniku korzystam z funkcji rekurencyjnej 'getcode', która dla danego liścia, idzie po rodziach w górę,
#  aż dojdzie do elementu bez rodzica, i wychodząc z odpowiednich instancji, wypisuje po której stronie (self.side)
#  się znajduje (lewo->0 ; prawo->1)
#  przy wypisywaniu kodu dla każdej litery sprawdzam głębokość (depth) ścieżki prowadzącej do danego liścia, otrzymując
#  tym samym długość kodu, jeżeli dla każdej listery pomnożymy długość jej kodu przez częstość jej występowania, otrzy-
#  mamy długość całego napisu
#  złożonośc obliczeniowa tej części to O(n^2), ponieważ może zdarzyć się przypadek, gdy dla O(n) liści dłogość kodu
#  jest na poziomie O(n)


from queue import PriorityQueue


class Node:
    def __init__(self, v=None, l=None, n=None, s=None):
        self.val = v    # częstość występowania węzła
        self.let = l    # litera węzła (używana tylko w najniższych liściach drzewa, czyli elementy tablicy T)
        self.next = n   # wskazuje na rodzica danego węzła
        self.side = s   # atrybut side mówi nam na którym liściu jesteśmy: lewy->0 ; prawy->1

    # dwie poniższe metody odpowiadają za zrobienie obiektów mojej klasy Node porownywalnymi:
    def __gt__(self, other):
        return self.val > other.val

    def __lt__(self, other):
        return self.val < other.val


def huffman(S, F):
    def getcode(n):
        nonlocal depth
        if n.next is not None:
            depth += 1
            getcode(n.next)
            print(n.side, end='')
        return

    n = len(S)
    T = [Node(F[i], S[i]) for i in range(n)]
    T.sort(key=lambda x: x.let)     # sortuje elementy wzglęcem pola z literą

    pq = PriorityQueue(maxsize=n)   # inicjalizacja koleji prioretytowej
    for i in range(n):
        pq.put(T[i])

    while pq.qsize() > 1:   # dopóki nie zostanie mi tylko jeden Node, czyli dopóki nie stworzę kompletnego drzewa
        l = pq.get()
        l.side = 0
        r = pq.get()
        r.side = 1
        new = Node(l.val + r.val)
        l.next = new
        r.next = new
        pq.put(new)

    length = 0
    depth = 0

    for item in T:
        print(f"{item.let} : ", end='')
        getcode(item)
        print()
        length += depth * item.val
        depth = 0

    print(f"dlugosc napisu: {length}")


S = ["a", "b", "c", "d", "e", "f"]
F = [10, 11, 7, 13, 1, 20]
huffman(S, F)
