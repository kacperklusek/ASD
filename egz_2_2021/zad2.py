from zad2testy import runtests


# O(n)
# dla każdego node wyznaczam wartość poddrzewa zakorzenionego w nim
# potem liniowo przechodzę po drzewie i sprawdzam która krawędź spełnia warunki zadania

def get_weights(root):
    if len(root.weights) == 0:
        return 0

    output = sum(root.weights)

    for e in root.edges:
        output += get_weights(e)

    root.tree = output

    return output


def balance(T):
    get_weights(T)

    best = float('inf')
    e = None
    whole_tree = T.tree

    def get_answer(root):
        nonlocal best, e, whole_tree

        n = len(root.weights)

        for i in range(n):
            if abs(whole_tree - 2 * root.edges[i].tree - root.weights[i]) < best:
                best = abs(whole_tree - 2 * root.edges[i].tree - root.weights[i])
                e = root.ids[i]
            get_answer(root.edges[i])

    get_answer(T)

    return e


runtests(balance)
