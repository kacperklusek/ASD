from zad3testy import runtests


# robie tablice l gdzie l[i] odpowiada kolorowi lampki i, i dla każdej operacji zmieniam kolory lampek w
# podanym przedziale, podczas zmiany koloru lampki zliczam ile świeci się na niebiesko w danej chwili
# na początku każda świeci się na zielono więc nie muszę wtedy liczyć
# złożoność n + T



def lamps( n,T ):
    # l = [0 for _ in range(n)]
    l = [0] * n

    result = 0
    counter = 0

    for left, right in T:
        for i in range(left, right+1):
            l[i] += 1
            l[i] %= 3
            if l[i] == 2:
                counter += 1
            elif l[i] == 0:
                counter -= 1

        result = max(result, counter)

    return result

    
runtests( lamps )


