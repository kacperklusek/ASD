from zad3testy import runtests

# Kacper Kłusek
# iteruje po indeksach w C, następnie dla każdego tego indeksu odtwarzam jego ścieżkę do korzenia, i z korzenia
# po zapamiętanej ścieżce idę do odpowiedniego node'a, pobierając jego wartość i następnie porównując z największą
# do tej pory zapamiętaną
# złożoność obliczeniowa algorytmu to O(mlogn), a pamięciowa O(logn)


def left(i):
    return 2*i

def right(i):
    return 2*i+1

def parent(i):
    return i//2


def get_key(T, idx):
    path = []
    while idx >= 1:
        path.append(idx)
        idx //= 2

    idx = path.pop(len(path)-1)

    while path:
        target = path.pop(len(path)-1)
        if target == right(idx):
            T = T.right
            idx = target
        elif target == left(idx):
            T = T.left
            idx = target

    return T.key


def maxim( T, C ):
    m = float('-inf')

    for idx in C:
        key = get_key(T, idx)
        m = max(m, key)

    return m



    
runtests( maxim )


