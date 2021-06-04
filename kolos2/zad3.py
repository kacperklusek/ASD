from zad3testy import runtests
from queue import PriorityQueue

# algorytm zahcłanny:
# wybieram największą plamę ropy jaka jest, sprawdzam zasięg czy dam radę dojechać do końca tablicy, jeśli nie, to
# wybieram znowu największą stację w zasięgu
# zawsze opłaca mi się zatzymać na największej plamie żeby mieć największy zasięg, bo mogę tankować do pełna, ile chce
# bo mam niograniczony bak
#
# złożoność algorytmu to O(n²), bo w najgorszym przypadku na co drugim polu byłaby plama ropy o objetosci 2
# wtedy musielibyśmy n/2 razy sprawdzać największą plamę w zasięgu O(n)



def linearize(T):
    n = len(T[0])
    m = len(T)

    def collect(j, i=0):
        nonlocal T, ropa, n, m

        if T[i][j] > 0:
            ropa += T[i][j]
            T[i][j] = 0
        else:
            return

        if i-1 >= 0 and T[i-1][j] > 0 :
            collect(j, i-1)
        if i+1 < m and T[i + 1][j] > 0 :
            collect(j, i+1)
        if j+1 < n and T[i][j+1] > 0 :
            collect(j+1, i)
        if j-1 >= 0 and T[i][j-1] > 0:
            collect(j-1, i)

    new = [0 for _ in range(n)]
    for i in range(n):
        ropa = 0
        collect(i)
        new[i] = ropa

    return new



def plan(T):
    T = linearize(T)
    # print('nowa tablica ->>>>>>>>>>>' ,T)
    n = len(T)

    stations = PriorityQueue()
    for i in range(1, min(n, T[0]+1)):
        if T[i] > 0:
            stations.put((-T[i], -i))

    refueling = [0]
    rng = T[0]

    while rng+1 < n:
        biggest_station, bs_idx = stations.get()
        biggest_station *= -1
        bs_idx *= -1
        for i in range(rng + 1, min(n, rng + biggest_station + 1)):
            if T[i] > 0:
                stations.put((-T[i], -i))

        rng += biggest_station
        refueling.append(bs_idx)

    refueling.sort()

    return refueling


runtests(plan)
