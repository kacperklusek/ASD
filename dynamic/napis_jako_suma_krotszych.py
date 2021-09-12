def max_width(S, t):
    n = len(S)
    N = len(t)

    # f[i] - maksymalna minimalna szerokość podnapisu t[:i] ze słownika S
    f = [0 for _ in range(N+1)]


    for i in range(1, N+1):
        for j in range(n):
            if t[:i] == S[j]:
                f[i] = i
            else:
                l = len(S[j])
                if t[i-l : i] == S[j]:
                    f[i] = max(f[i], min(f[i-l], l))

    return f[N]





S = ['ab', 'abab', 'ba', 'bab', 'b']
t = 'ababbab'

print(max_width(S, t))
