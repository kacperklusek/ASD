from zad2testy import runtests


class Node:
    def __init__(self):
        self.left = None  # lewe podrzewo
        self.leftval = 0  # wartość krawędzi do lewego poddrzewa jeśli istnieje
        self.right = None  # prawe poddrzewo
        self.rightval = 0  # wartość krawędzi do prawego poddrzewa jeśli istnieje
        self.X = None  # dodatkowe dane


def valuableTree(T: Node, k):
    size = k
    T.X = [[None for _ in range(k + 1)], [None for _ in range(k + 1)]]

    # największe podrzewo zawierające k krawedzie pod nodem T, zawierające node T
    def f(T: Node, k):
        nonlocal size
        if T.X is None:
            T.X = [[None for _ in range(size + 1)], [None for _ in range(size + 1)]]

        if k > 0 and T.left is None and T.right is None:
            return float('-inf')

        if k == 0:
            T.X[0][k] = 0
            return 0

        if T.X[0][k] is not None:
            return T.X[0][k]

        # biore prawą i lewą krawędź
        if T.left is not None and T.right is not None:
            for i in range(k - 1):  # k-2+1
                if T.X[0][k] is not None:
                    T.X[0][k] = max(T.X[0][k], T.rightval + T.leftval + f(T.left, k - 2 - i) + f(T.right, i))
                else:
                    T.X[0][k] = T.rightval + T.leftval + f(T.left, k - 2 - i) + f(T.right, i)

        # biorę tylko lewą krawędź
        if T.left is not None:
            if T.X[0][k] is not None:
                T.X[0][k] = max(T.X[0][k], T.leftval + f(T.left, k - 1))
            else:
                T.X[0][k] = T.leftval + f(T.left, k - 1)

        # biorę tylko prawą krawędź
        if T.right is not None:
            if T.X[0][k] is not None:
                T.X[0][k] = max(T.X[0][k], T.rightval + f(T.right, k - 1))
            else:
                T.X[0][k] = T.rightval + f(T.right, k - 1)

        return T.X[0][k]

    # największe podrzewo zawierające k krawędzi pod nodem T, nie zawierające node T
    def g(T: Node, k):
        nonlocal size
        if T.X is None:
            T.X = [[None for _ in range(size + 1)], [None for _ in range(size + 1)]]

        if k > 0 and (T.left is None and T.right is None):
            return float('-inf')

        if k == 0:
            T.X[1][k] = 0
            return 0

        if T.X[1][k] is not None:
            return T.X[1][k]

        # są obie krawędzie
        if T.left is not None and T.right is not None:
            if T.X[1][k] is not None:
                T.X[1][k] = max(T.X[1][k], g(T.left, k), g(T.right, k), f(T.left, k), f(T.right, k))
            else:
                T.X[1][k] = max(g(T.left, k), g(T.right, k), f(T.left, k), f(T.right, k))

        # jest tylko lewa krawedz
        elif T.left is not None and T.right is None:
            if T.X[1][k] is not None:
                T.X[1][k] = max(T.X[1][k], f(T.left, k), g(T.left, k))
            else:
                T.X[1][k] = max(f(T.left, k), g(T.left, k))

        # jest tylko prawa krawedz
        elif T.right is not None and T.left is None:
            if T.X[1][k] is not None:
                T.X[1][k] = max(T.X[1][k], f(T.right, k), g(T.right, k))
            else:
                T.X[1][k] = max(f(T.right, k), g(T.right, k))

        return T.X[1][k]

    # a= f(T, k)
    # b= g(T, k)

    return max(f(T, k), g(T, k))


runtests(valuableTree)


