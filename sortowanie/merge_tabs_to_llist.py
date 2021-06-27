class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


def foo(T):
    n = len(T)
    indices = [0 for _ in range(n)]

    def get_idx(T):
        nonlocal indices
        aux = -1
        for i in range(n):
            aux = i if indices[i] < len(T[i]) and (T[i][indices[i]] < aux or aux < 0) else aux
        # indices[aux] += 1
        return aux if aux > 0 else None

    nd = Node(T[get_idx(T)][0]) # 0 bo to pierwszy element

    first = nd
    while 1:
        idx = get_idx(T)
        if idx is None:
            break
        nd.next = Node(T[idx][indices[idx]])
        indices[idx] += 1
        nd = nd.next

    return first