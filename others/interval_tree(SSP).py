from math import log2, ceil


def parent(x):
    return (x - 1) // 2


def left(x):
    return 2 * x + 1


def right(x):
    return 2 * x + 2


def create_inttree_SSP(K):
    K = [(K[i], i, i+1) for i in range(len(K))]

    # rozszerzam tablicę żeby była wielokrotnością dwójki
    target_len = 2 ** ceil(log2(len(K)))
    while len(K) < target_len:
        K.append((0, len(K), len(K)+1))

    # teraz dodaje na początek tablicy n-1 elementów, żebym mógł zrobić tablicową reprezentacje drzewa
    K = [0 for _ in range(len(K) - 1)] + K

    for i in range(len(K) - 1, 1 - 1, -2):
        val, l, r = K[i - 1][0] + K[i][0], K[i - 1][1], K[i][2]
        K[parent(i)] = (val, l, r)

    return K

def get_result(T, p, k, i):
    if T[i][1] == p and T[i][2] == k:
        return T[i][0]
    else:
        ll, lr, rl, rr = T[left(i)][1], T[left(i)][2], T[right(i)][1], T[right(i)][2]
        if ll <= p < k <= lr:
            return get_result(T, p, k, left(i))
        elif rl <= p < k <= rr:
            return get_result(T, p, k, right(i))
        else:
            return get_result(T, p, lr, left(i)) + get_result(T, rl, k, right(i))


# zwraca sumę elementów K[p:k], czyli od p do k-1 włącznie
def SSP(K, p, k):
    ssp = create_inttree_SSP(K)

    if p == k:
        return K[p]

    result = get_result(ssp, p, k, 0)

    return result



K = [4, 2, 3, 5, 67, 4, 3, 36, 7, 3, 3, 54]

print(SSP(K, 2, 5))
