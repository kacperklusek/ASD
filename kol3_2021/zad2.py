from zad2testy import runtests


# opis algorytmu:
# dla każdego z dzieci roota (ozn. node) wyznaczam rekurencyjnie najmniejszą wartość 'f' jaką można osiągnąć odcinając
# liście od korzenia jako f = min(node.value, f(lewe dziecko) + f(prawe dziecko)) jeśli istnieją oboje dzieci
# jeśli istnieje tylko lewe dziecko, to wiadomo że opłaca się odciąć niżej bo po lewej jest mniejsza wartość
# jeśli istnieje tlyko prawe dziecko to odcinamy przy node, bo po prawej będą tylko większe wartości
# nie będzie sytuacji w której nie istnieją oboje dzieci bo rozważam tylko wierchołki niebędące liściami
# jeśli oboje dzieci  są liściami to mogę odciąć je od roota tylko przez odcięcie node czyli f(node) = node.value
#
# złożoność obliczeniowa algorytmu to O(n), gdzie n to liczba wierzchołków w drzewie BST


class BNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


def is_before_leaf(node: BNode):
    left_ok = False
    right_ok = False
    if node.left is not None:
        if node.left.left is None and node.left.right is None:
            left_ok = True
    else:
        left_ok = True
    if node.right is not None:
        if node.right.left is None and node.right.right is None:
            right_ok = True
    else:
        right_ok = True
    return left_ok and right_ok


def is_leaf(node: BNode):
    if node.left is None and node.right is None:
        return True
    return False


def do_the_cut(node: BNode):
    if is_before_leaf(node):
        return node.value
    else:
        if node.right is None and node.left is not None:
            return do_the_cut(node.left)
        elif node.left is None and node.right is not None:
            return node.value
        elif is_leaf(node.left) or is_leaf(node.right):
            return node.value
        return min(node.value, do_the_cut(node.left) + do_the_cut(node.right))


def cutthetree(T: BNode):
    if T.left is None and T.right is not None:
        best_cut = do_the_cut(T.right)
    elif T.right is None and T.left is not None:
        best_cut = do_the_cut(T.left)
    else:
        best_cut = do_the_cut(T.left) + do_the_cut(T.right)

    return best_cut

runtests(cutthetree)
