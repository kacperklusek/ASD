from zad1testy import runtests

# # pierwszy pomysł; dla każdej literki sprawdzam, czy w drugim słowie jest taka sama literka w kole o radius'ie == t
# # O(nt)
# def tanagram(x, y, t):
#     n = len(x)
#     if n != len(y):
#         return False
#
#     used = [0 for _ in range(n)]
#
#     for i in range(n):
#         found = 0
#         for r in range(max(0, i-t), min(i+t + 1, n)):
#             if not used[r] and y[r] == x[i]:
#                 used[r] = 1
#                 found = 1
#                 break
#         if not found:
#             return False
#
#     return True


# 2nd idea
# wpisuje dla każdej litery z y indeksy na których występuje w słowie y
# O(n)
def tanagram(x, y, t):
    n = len(x)
    if n != len(y):
        return False

    letters = [[] for _ in range(26)] # 26 bo to wielkość afabetu bez polskich znaków : abcdefghijklmnopqrstuwvqxyz
    idx = [0 for i in range(26)]

    # uzupełniam w tablicy letters indeksy liter ze słowa y O(n)
    for i in range(n):
        letters[ord(y[i]) - ord('a')].append(i)

    # dla każdej z x sprawdzam czy ma odpowiadającą litere na pozycjach od i-t do i+t
    for i in range(n):
        let = x[i]
        key = ord(let) - ord('a')
        if i-t <= letters[key][idx[key]] <= i+t:
            idx[key] += 1
        else:
            return False

    return True



runtests( tanagram )