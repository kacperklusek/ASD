from zad1testy import runtests

def get_min(root):
    while root.left is not None:
        root = root.left
    return root

def get_succ(node):
    if node.right is not None:
        return get_min(node.right)
    else:
        node = climb_leftwards(node)  # climb right branch until it's possible (climb leftwards)
        node = node.parent if node.parent is not None else None  # then jump to parent (jump right) if exists
        return node


def climb_leftwards(root):
    while root.parent is not None and root.parent.right is root:
        root = root.parent
    return root


def ConvertTree(p):
    tab = []

    aux = get_min(p)
    root = aux

    while aux is not None:
        tab.append(aux)
        aux = get_succ(aux)

    n = len(tab)

    def left(i):
        return 2 * i + 1

    def right(i):
        return 2 * i + 2

    root.left = tab[1]
    root.right = tab[2]
    tab[1].parent = tab[0]
    tab[2].parent = tab[0]
    span = [1, 2]

    while span[0] < n:
        for idx in range(span[0], span[1]+1):
            if idx < n and tab[idx] is not None:
                tab[idx].left  = tab[left(idx)] if left(idx) < n else None
                tab[idx].right = tab[right(idx)] if right(idx) < n else None
                if left(idx) < n:
                    tab[left(idx)].parent = tab[idx]
                if right(idx) < n:
                    tab[right(idx)].parent = tab[idx]

        span = [left(span[0]), right(span[1])]

    return root







runtests( ConvertTree )