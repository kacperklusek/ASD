def is_there_a_sum(t, x):
    l, r = 0, len(t)-1
    while t[l] + t[r] != x and l < r:
        if t[r] + t[l] > x:
            r -= 1
        else:
            l += 1
    return (True, l, r) if l < r else False

print(is_there_a_sum([1,2,3,4,5,6,7,8,9], 5))

