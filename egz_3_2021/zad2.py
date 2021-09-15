from zad2testy import runtests

# Kacper Kłusek
# brute force:
# rozważam każdy prefix z listy L
# i sprawdzam po kolei czy jest fajny i potem czy bardzo fajny

# złożoność O(n^3 * m) gdzie n to len(L) a m to długość najdłuższego słowa w L


def is_prefix(word, quest):
    n = len(word)
    if len(word) > len(quest):
        return False
    for i in range(n):
        if word[i] != quest[i]:
            return False
    return True


def is_cool(L, word):
    n = len(L)
    cnt = 0
    prev = 0
    for i in range(n):
        if is_prefix(word, L[i]):
            cnt += 1
            prev += 1
        if prev and cnt < 2:
            return False
        if cnt >= 2:
            return True
    return False


def is_very_cool(L, word):
    n = len(word)
    word += '0'
    if is_cool(L, word):
        return False
    word = word[:n]
    word += '1'
    if is_cool(L, word):
        return False
    return True


def double_prefix( L ):
    output = []
    used = []

    for item in L:
        for i in range(1, len(item)):
            word = item[:i]

            if word in output or word in used:
                continue
            used.append(word)

            if not is_cool(L, word):
                continue
            if is_very_cool(L, word):
                output.append(word)

    return output


runtests( double_prefix )

