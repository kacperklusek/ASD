from zad2testy import runtests


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __gt__(self, other):
        return self.val > other.val

def insert_k(prev, node, end):
    min = node
    aux = node
    prev_min = prev

    # wybieram najmniejszy node (val) najdalej k nodeów od node
    while aux is not end:
        prev_min = aux
        aux = aux.next
        if aux is None:
            return node, end
        min = aux if aux.val < min.val else min

    # podmieniam node z minimum
    if node.next is min:
        prev.next = min
        node.next = min.next
        min.next = node
    elif node is not min:
        prev.next, node.next, min.next, prev_min.next = min, min.next, node.next, node

    return (min, end) if end is not min else (min, node)


def SortH(p: Node, k):
    end = p
    for i in range(k):
        if end is not None:
            end = end.next

    wart = Node()
    wart.next = p
    start, end = insert_k(wart, p, end)

    while end is not None:
        prev = p
        p = p.next
        end = end.next
        p, end = insert_k(prev, p, end)

    return start


runtests(SortH)
