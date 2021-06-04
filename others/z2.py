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

    def insert(self, value):
        q = self
        new = Node(value)
        while q.next is not None and q.next.val < value:
            q = q.next
        q.next, new.next = new, q.next


'''
    j q
    p m
w 5 3 9 4
'''

def get_max(first):
    wart = Node(None, first)
    p, j = wart, wart
    q, m = first, first
    p.next = m.next
    while q is not None:
        if q.val > m.val:
            p.next = m
            p, m = j, q
            p.next = m.next
        else:
            j, q = q, q.next

    return wart.next, m


def selection_sort(first):
    s_list = None
    unsorted_list, m = get_max(first)
    while unsorted_list is not None:
        m.next = s_list
        s_list = m
        unsorted_list, m = get_max(unsorted_list)
    m.next = s_list
    s_list = m

    return s_list


llist = Node(2, (Node(53, Node(532, Node(3, Node(421, Node(55, Node(99, Node(1, Node(12, Node(0)))))))))))
llist = selection_sort(llist)
print(llist)
llist.insert(13)
print(llist)


