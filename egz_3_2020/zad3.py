from zad3testy import runtests


class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


def foo(T):
    n = len(T)

    def get_idx(T):
        aux = -1
        for i in range(n):
            aux = i if T[i] is not None and (T[i].val < T[aux].val or aux < 0) else aux
        return aux if aux >= 0 else None

    nd = T[get_idx(T)]  # 0 bo to pierwszy element
    T[get_idx(T)] = T[get_idx(T)].next
    first = nd

    while 1:
        idx = get_idx(T)
        if idx is None:
            break
        nd.next = T[idx]
        T[idx] = T[idx].next
        nd = nd.next

    return first


runtests(foo)
