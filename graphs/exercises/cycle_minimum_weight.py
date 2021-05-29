"""
Offline exercise nr 9.
"""
from copy import deepcopy
from queue import PriorityQueue


def relax(dst, parent, infinity, v, u, weight_v_u):
    """Utility function for mod_dijkstra."""

    if infinity[u]:
        dst[u] = dst[v] + weight_v_u
        parent[u] = v
        infinity[u] = False
        return True

    if dst[u] > dst[v] + weight_v_u:
        dst[u] = dst[v] + weight_v_u
        parent[u] = v
        return True

    return False


def mod_dijkstra(graph, t, s=0):
    """Modified Dijkstra algorithm for shortest path between
    two vertices."""

    n = len(graph)
    queue = PriorityQueue()
    infinity = [True for _ in range(n)]
    distances = [-1 for _ in range(n)]
    parents = [None for _ in range(n)]

    distances[s] = 0
    infinity[s] = False
    queue.put((0, s))

    while not queue.empty():
        _, v = queue.get()
        for i in range(n):
            if graph[v][i] > 0:
                if relax(distances, parents, infinity, v, i, graph[v][i]):
                    queue.put((distances[i], i))

    pathvu = abs(distances[t])

    return parents, pathvu


def f(cycle, parents, u):
    """Store vertices of a cycle in list."""
    if parents[u] is not None:
        f(cycle, parents, parents[u])
    cycle.append(u)


def min_cycle(graph):
    """
    Function finds cycle in a graph with minimum weight.
    :param graph: matrix representation of a graph.
    :return: min weight cycle as a list.
    """
    edges = len(graph)
    min_weight = float("inf")
    cycle = []

    # for every edge
    for v in range(edges):
        for u in range(edges):
            if graph[v][u] > 0:
                # delete edge
                edge_weight = graph[v][u]
                graph[v][u] = graph[u][v] = 0

                # do dijkstra and return list of parents and shortest path between u and v
                parents, pathvu = mod_dijkstra(graph, u, v)
                # add weight of deleted edge
                pathvu += edge_weight
                if min_weight > pathvu:
                    min_weight = pathvu
                    cycle = [u]
                    f(cycle, parents, parents[u])

                # restore edge
                graph[v][u] = graph[u][v] = edge_weight

    return cycle


if __name__ == "__main__":
    G = [[-1, 2, -1, -1, 1],
         [2, -1, 4, 1, -1],
         [-1, 4, -1, 5, -1],
         [-1, 1, 5, -1, 3],
         [1, -1, -1, 3, -1]]
    LEN = 7

    GG = deepcopy(G)
    cycle = min_cycle(GG)

    print("Cykl :", cycle)

    if cycle == []:
        print("Błąd (1): Spodziewano się cyklu!")
        exit(0)

    L = 0
    u = cycle[0]
    for v in cycle[1:] + [u]:
        if G[u][v] == -1:
            print("Błąd (2): To nie cykl! Brak krawędzi ", (u, v))
            exit(0)
        L += G[u][v]
        u = v

    print("Oczekiwana długość :", LEN)
    print("Uzyskana długość   :", L)

    if L != LEN:
        print("Błąd (3): Niezgodna długość")
    else:
        print("OK")