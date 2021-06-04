def do_the_magic(T):
    n = len(T)
    output = [None]

    i = 0
    while i < n:
        start = T[i]
        i += 1
        stop = start + 1

        while i  < n and T[i] <= stop:
            i += 1

        output.append((start, stop))

    return output


T = [0.25, 0.5, 1.6]
print(do_the_magic(T))

