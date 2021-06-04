from random import seed, randint
from time import time
# ###############################
#
# def countSort(arr, n, exp):
#     output = [0] * n  # output array
#     count = [0] * n
#     for i in range(n):
#         count[i] = 0
#
#     # Store count of occurrences in count[]
#     for i in range(n):
#         count[(arr[i] // exp) % n] += 1
#
#     # Change count[i] so that count[i] now contains
#     # actual position of this digit in output[]
#     for i in range(1, n):
#         count[i] += count[i - 1]
#
#         # Build the output array
#     for i in range(n - 1, -1, -1):
#         output[count[(arr[i] // exp) % n] - 1] = arr[i]
#         count[(arr[i] // exp) % n] -= 1
#
#     # Copy the output array to arr[], so that
#     # arr[] now contains sorted numbers according
#     # to current digit
#     for i in range(n):
#         arr[i] = output[i]
#
#     # The main function to that sorts arr[] of
#
#
# # size n using Radix Sort
# def sort(arr, n):
#     # Do counting sort for first digit in base n.
#     # Note that instead of passing digit number,
#     # exp (n^0 = 1) is passed.
#     countSort(arr, n, 1)
#
#     # Do counting sort for second digit in base n.
#     # Note that instead of passing digit number,
#     # exp (n^1 = n) is passed.
#     countSort(arr, n, n)
#
#
#
#
#
#
#
# ##############################


def partition(T, l, r):
    last = l
    for i in range(l, r):
        if T[i] <= T[r]:
            T[i], T[last] = T[last], T[i]
            last += 1
    T[last], T[r] = T[r], T[last]
    return last


def quicksort(T):
    n = len(T)
    stack = []
    stack.append((0, n - 1))
    while stack:
        l, r = stack.pop()
        if l < r:
            q = partition(T, l, r)
            stack.append((l, q - 1))
            stack.append((q + 1, r))


def countsort_turbo_s(t, p, k):
    d = k-p
    newarr = [0 for _ in range(d)]
    for i in range(len(t)):
        newarr[(t[i]-p)] += 1

    idx = 0
    for i in range(len(newarr)):
        while newarr[i] != 0:
            t[idx] = p+i
            idx += 1
            newarr[i] -= 1


def sort_many(t):
    n = len(t)
    new_arr = [[] for i in range(n)]
    for i in range(n):                  # [ 1, 6, 9, 11, 20]
        new_arr[t[i]//n].append(t[i])   # [[][ ][ ]

    idx = 0
    for i in range(n):
        if len(new_arr[i]) > 1:
            if len(new_arr[i]) > n**(1/2):
                # print('+')
                countsort_turbo_s(new_arr[i], n*i, n*i + n)
            else:
                quicksort(new_arr[i])
            for j in range(len(new_arr[i])):
                t[idx] = new_arr[i][j]
                idx += 1
        elif len(new_arr[i]) == 1:
            t[idx] = new_arr[i][0]
            idx += 1


total = 0
n = 40000
l_testow = 50
for _ in range(l_testow):
    start = time()
    t = [randint(0, 5*n) for _ in range(n)]
    # print('lista przed sortowaniem: ', t)
    sort_many(t)
    # print('lista po sortowaniu: ', t)
    stop = time()
    total += stop-start
    # print(stop-start)

print(f'sredni czas dla tablicy o n={n}: ', total/l_testow)



total = 0
for _ in range(l_testow):
    start = time()
    t = [randint(0, 5*n) for _ in range(n)]
    # print('lista przed sortowaniem: ', t)
    quicksort(t)
    # print('lista po sortowaniu: ', t)
    stop = time()
    total += stop-start
    # print(stop-start)

print(f'sredni czas dla tablicy o n={n}: ', total/l_testow)
