# F[i][t] = (1) if there is a subarray from index 0 to i, which sum is t else (0)
# F[i][0] = 1 for every i
# F[0][t] = 0 if A[0] != t else 1
# F[i][t] for every elem in A, check if you can notate 't' as A[i] + F[i-1][t-A[i]]; 1 if yes 0 if no

def print_solution(A, t, F, idx):
    if t > 0:
        if idx > 0 and F[idx-1][t] == 1:
            print_solution(A, t, F, idx-1)
        else:
            print_solution(A, t-A[idx], F, idx-1)
            print(A[idx], end=' ')


def SOS(A, t):
    if t == 0:
        return True

    n = len(A)
    F = [[0] * (t+1) for _ in range(n)]

    mn = A[0]
    for i in range(n):
        F[i][0] = 1
        mn = min(A[i], mn)

    if mn > t:
        return False

    F[0][A[0]] = 1

    for i in range(n):
        for j in range(t+1):
            F[i][j] = F[i-1][j]     # case in which you can notate j as a sum of elements from 0 to n-1
            if F[i][j] == 0:
                F[i][j] = 1 if F[i-1][j-A[i]] == 1 else 0   # case in which you can add current elem to existing sum

    output = False
    idx = 0

    for i in range(n):
        if F[i][t] == 1:
            output = True
            idx = i
            break

    if output:
        print_solution(A, t, F, idx)
        print()

    return output


# F[i] istnieje suma podciagu rowna i
def SOS_flat(A, t):
    if t == 0:
        return True

    n = len(A)
    F = [False for _ in range(t+1)]
    F[0] = True

    for i in range(n):
        for j in range(t-A[i], -1, -1):
            if F[j]:
                F[j+A[i]] = True

    return F[t]



a = [2, 2, 3, 5, 2, 2, 2]
for t in range(1, 20):
    print('nie' if SOS(a, t) != SOS_flat(a, t) else 'tak')
