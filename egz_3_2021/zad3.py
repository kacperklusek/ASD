from zad3testy import runtests
from math import log2


# Kacper Kłusek
#
# iteruje po indeksach w C, następnie dla każdego tego indeksu schodzę w dół drzewa decydując na bierząco w którą stronę
# powinienem zejść
# decyzja odbywa sie tak:
# znam dwie skrajne (lewa i prawa) wartośći rzędu  w którym znajduje się szukany indeks; sprawdzam, po której stronie
# tego rzędu znajduje się indeks, i odpowiednio zmieniam swoje położenie w drzewie.
# Jak zmienie położenie to muszę też zawęzić szukany rząd, do jego prawej lub lewej połowy w zależności od 'skoku'
# (w prawo lub lewo), ponieważ wtedy ta połowa rozważanego rzędu staje się całym ostatnim rzędem 'nowego' poddrzewa
#
# złożoność obliczeniowa algorytmu to O(mlogn), a pamięciowa O(1)


def left_child(i):
    return 2 * i


def right_child(i):
    return 2 * i + 1


def get_key(T, idx):
    row_idx = int(log2(idx))
    actual_idx = 1
    left, right = 2 ** row_idx, 2 ** (row_idx + 1) - 1  # lewa i prawa granica (indeksy) rzędu w którym jest idx

    while actual_idx != idx:
        # idx znajduje się w lewej części rozważanego poddrzewa
        if idx <= (left + right) // 2:
            T = T.left
            actual_idx = left_child(actual_idx)
            right = (left + right) // 2

        # idx znajduje się w prawej części rozważanego poddrzewa
        elif idx > (left + right) / 2:
        # lub po prostu else zamiast elif
            T = T.right
            actual_idx = right_child(actual_idx)
            left = (left + right) // 2 + 1

    return T.key


def maxim(T, C):
    m = float('-inf')

    for idx in C:  # O(m)
        key = get_key(T, idx)  # O(logn)
        m = max(m, key)

    return m


runtests(maxim)
