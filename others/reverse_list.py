class Node:
    def __init__(self, v=None, n=None):
        self.val = v
        self.next = n

    def __str__(self):
        n = self
        strr = ''
        while n is not None:
            strr += str(n.val) + ' '
            n = n.next
        return strr

    # def insert(self, value):
    #     q = self
    #     new = Node(value)
    #     while q.next is not None and q.next.val < value:
    #         q = q.next
    #     q.next, new.next = new, q.next


def rev(first):
    q = first
    if q.next is None:
        return q
    prev = None
    while q is not None:
        q.next, q, prev = prev, q.next, q

    return prev


#   p q n N
# n 1 5 6 7 9
llist = Node(2, (Node(53, Node(532, Node(3, Node(421, Node(55, Node(99, Node(1, Node(12, Node(0)))))))))))
print(llist)
llist = rev(llist)
print(llist)
