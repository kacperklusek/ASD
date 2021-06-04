class Node:
    def __init__(self, name=None):
        self.name = name
        self.children = 0
        self.child = []
        self.max_ending = 0
        self.max_through = 0


def heavy_path(T):
    def fulfill(node):
        nonlocal max_path
        if len(node.child) == 0:
            return 0, 0

        ending = 0
        ending_2nd = 0
        for child, cost in node.child:
            child.max_ending, child.max_through = fulfill(child)

            temp = child.max_ending + cost
            ending_2nd = ending if ending < temp else max(ending_2nd, temp)
            ending = max(ending, temp)

        node.max_ending = ending
        node.max_through = ending + ending_2nd

        max_path = max(max_path, node.max_ending, node.max_through)

        return node.max_ending, node.max_through

    max_path = 0
    fulfill(T)

    return max_path



# A = Node('a')
# B = Node('b')
# C = Node('c')
#
# D = Node('d')
# E = Node('e')
# F = Node('f')
# G = Node('g')
# H = Node('h')
#
# A.child = [(B, 5), (C, -1)]
# B.child = [(D, -3), (E, 6), (F, 2)]
# C.child = [(G, 4), (H, 2)]


A = Node()
B = Node()
C = Node()
D = Node()
E = Node()
F = Node()
G = Node()
H = Node()
I = Node()
J = Node()
A.children = 2
B.children = 2
E.children = 3
F.children = 1
G.children = 1
A.child = [(B, 4), (E, -2)]
B.child = [(C, 4), (D, -2)]
E.child = [(F, 4), (G, 5), (I, 2)]
F.child = [(H, 3)]
G.child = [(I, -10)]


print(heavy_path(A))


