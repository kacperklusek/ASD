def bubble(t):
    for k in range(len(t) - 1):
        for i in range(len(t) - 1 - k):
            if t[i] > t[i + 1]:
                t[i], t[i + 1] = t[i + 1], t[i]

    return t

    # for d in range(1, len(t)-1):
    #     while d >= 0 and t[d+1] < t[d]:
    #         t[d+1], t[d] = t[d], t[d+1]
    #         d -= 1
def insertion(t):
    for d in range(1, len(t)-1):
        for i in range(d, -1, -1):
            if t[i] > t[i+1]:
                t[i+1], t[i] = t[i], t[i+1]
            else:
                break
    return t

def selection(t):

    def find_min(tab, p):
        m = (tab[p], p)
        for i in range(p, len(tab)):
            if tab[i] < m[0]:
                m = (tab[i], i)
        return m[1]

    for p in range(len(t)):
        idx = find_min(t, p)
        t[p], t[idx] = t[idx], t[p]

    return t


print(bubble([5, 6,1,3213,321, 4, 7, 1, 421, 412, 42, 53, 647, 3, 31, 643, 64]))
print(insertion([5, 6,1,3213,321, 4, 7, 1, 421, 412, 42, 53, 647, 3, 31, 643, 64]))
print(selection([5,1,3213,321, 6, 4, 7, 1, 421, 412, 42, 53, 647, 3, 31, 643, 64]))

