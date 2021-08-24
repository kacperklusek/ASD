
def binsearch(tab, val):
    n = len(tab)
    l, r = 0, n-1
    while l < r:
        idx = (l + r) // 2
        if tab[idx] < val:
            l = idx+1
        elif tab[idx] > val:
            r = idx-1
        else:
            return idx
    return False


