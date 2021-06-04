def find(t, x):
    l = len(t)
    if l == 0:
        return None
    elif x == t[l//2]:
        i = l//2
        while i >= 0 and t[i] == x:
            i -= 1
        return i+1
    elif x > t[l//2]:
        i = find(t[(l//2) + 1:], x)
        return i + l//2 + 1 if i is not None else None
    else:
        i = find(t[:(l//2)], x)
        return i if i is not None else None

print(find([1,2,3,3,3,3,3,3,3,3,3, 5, 6, 9, 10, 15, 16, 16, 19], 9))
