
def parent(x):
    return int((x-1)/2)

def left(x):
    return 2*x + 1

def right(x):
    return 2*x + 2

def intersect(interval1, interval2):
    # returns True if interval 1 intersects with interval 2 else False
    if interval2[0] < interval1[0] < interval2[1] or\
        interval2[0] < interval1[1] < interval2[1] or\
        interval2 == interval1:
        return True
    else:
        return False

def rotate(tree):
    tree

def place_interval(tree, interval, i=0):
    if tree[i] is None:
        if i == right(parent(i)):
            tree[i] = [interval[0], interval[1], tree[parent(i)][2]+1]
            return 1
        else:
            tree[i] = [interval[0], interval[1], tree[parent(i)][2]]
            return 0

    elif intersect(interval, tree[i]):
        tree[i] = [min(tree[i][0], interval[0]), max(tree[i][1], interval[1]), tree[i][2]]
        add = place_interval(tree, interval, right(i))
        tree[i][2] += add

    else:
        add = place_interval(tree, interval, left(i))
        tree[i][2] += add

        if tree[right(i)] is None or tree[left(i)][2] > tree[right(i)][2]:
            rotate(tree)



def block_height(K):
    n = len(K)

    K = [i[2] * (i[0], i[1]) for i in K for _ in range(i[2])]

    tree = [None for _ in range(2*len(K))]
    tree[0] = [K[0][0], K[0][1], 1]

    for interval in K[1:]:
        place_interval(tree, interval)



K1 = [(1, 3, 1), (2, 5, 2), (0, 3, 2), (8, 9, 3), (4, 6, 1)]
R1 = 5

K2 = [(1, 3, 1), (2, 4, 1), (3, 5, 1), (4, 6, 1), (5, 7, 1), (6, 8, 1)]
R2 = 6

K3 = [(1, 10 ** 10, 1)]
R3 = 1

TESTY = [(K1, R1), (K2, R2), (K3, R3)]

good = True
for KK, RR in TESTY:
    print("Klocki           : ", KK)
    print("Oczekiwany wynik : ", RR)
    WW = block_height(KK)
    print("Otrzymany wynik  : ", WW)
    if WW != RR:
        print("Błąd!!!!")
        good = False

if good:
    print("OK!")
else:
    print("Problemy!")
