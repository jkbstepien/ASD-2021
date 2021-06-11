"""
Given an undirected connected graph, check if it contains any
cycle or not using the union-find algorithm.

Algorithm:
    1. Create disjoint sets for each vertex of the graph.
    2. For every edge u, v:
        i) Find the root of the sets to which elements u and v belongs.
        ii) If both u and v have the same root in disjoint sets, we've
            found a cycle.
"""


class Node:

    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent = self


def find_set(x):
    if x != x.parent:
        x.parent = find_set(x.parent)
    return x.parent


def make_set(n):
    return Node(n)


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    elif x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def cycle_uf_adj(graph):
    n = len(graph)
    sets = []

    for i in range(n):
        sets.append(make_set(i))

    for u in range(n):
        x = find_set(sets[u])
        for v in graph[u]:
            if u != v:
                y = find_set(sets[v])
                if x == y:
                    return True
                else:
                    union(x, y)

    return False


def main():
    graph1 = [
        [1],
        [2],
        [3, 4],
        [0],
        []
    ]
    print(cycle_uf_adj(graph1))


if __name__ == "__main__":
    main()
