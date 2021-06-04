class Node:
    def __init__(self, v):
        self.value = v
        self.neighbours = []
        self.side = None


def is_dichotomic(graph):

    for v in graph:

        # if neighbour is on the same side as v, graph is not dichotomic
        if v.side == 1:
            for nei in v.neighbours:
                if nei.side is not None:
                    if nei.side == 1:
                        return False
                else:
                    nei.side = 0
        # same here as above
        elif v.side == 0:
            for nei in v.neighbours:
                if nei.side is not None:
                    if nei.side == 0:
                        return False
                else:
                    nei.side = 1

        # if v is not assigned to any side, we search if any of his neighbours is and at once check if neighbours are
        # on the same side
        else:
            side_of_neighbours = None
            # checking what side neighbours should be on
            for nei in v.neighbours:
                if nei.side is not None:
                    side_of_neighbours = nei.side
                    break

            # if any of neighbours is assigned to any side
            if side_of_neighbours is not None:
                v.side = 1 if side_of_neighbours == 0 else 0
            # else, it means neither v nor any of neighbours is assigned to any side
            else:
                v.side = 0
                side_of_neighbours = 1

            # we fill unassigned neighbours and check for eventual collision
            for nei in v.neighbours:
                if nei.side is None:
                    nei.side = side_of_neighbours
                elif nei.side != side_of_neighbours:
                    return False

    return True


            # side = v.neighbours[0].side      # jakby był nie spójny to tu poprawić
            # for nei in v.neighbours:
            #     if nei.side is not None:    # neigh is assigned to side
            #         if side is not None and nei.side != side:   # if any previous neighbour was assigned to either side
            #             return False                            # and it was other side than one in current neigh
            #         else:   # elif side is None
            #             side = nei.side     # case in which nei is the first neighbour assigned to either side
            #
            # if side is None:    # in this case, neither neighbours nor v is assigned to any side
            #     v.side = 0
            #     for nei in v.neighbours:
            #         nei.side = 1
            # else:   # neighbours are not coliding and at least one of them is assigned to either side
            #     v.side = 1 if side == 0 else 0
            #     for nei in v.neighbours:
            #         if nei.side is None:
            #             nei.side = side

    # return True


gr = [Node(i) for i in range(8)]
# dichotomic
gr[0].neighbours = [gr[2]]
gr[1].neighbours = [gr[2], gr[3], gr[7]]
gr[2].neighbours = [gr[1]]
gr[3].neighbours = [gr[1]]
gr[4].neighbours = [gr[5], gr[7]]
gr[5].neighbours = [gr[4], gr[6]]
gr[6].neighbours = [gr[5]]
gr[7].neighbours = [gr[1], gr[4]]
print(is_dichotomic(gr))

# not dichotomic
gr[0].neighbours = [gr[2]]
gr[1].neighbours = [gr[2], gr[3], gr[7]]
gr[2].neighbours = [gr[1]]
gr[3].neighbours = [gr[1]]
gr[4].neighbours = [gr[5], gr[7]]
gr[5].neighbours = [gr[4], gr[6], gr[7]]
gr[6].neighbours = [gr[5]]
gr[7].neighbours = [gr[1], gr[4], gr[5]]

print(is_dichotomic(gr))
