"""
Dany jest graf nieskierowany G = (V,E) z ważonymi krawędziami (w: E -> N).
Proszę zaproponować jak najszybszy algorytm, który znajduje ścieżkę z danego
wierzchołka s do danego wierzchołka v, taką że:
    1. Każda kolejna krawędź ma mniejszą wagę niż poprzednia.
    2. Spośród ścieżek spełniających powyższy warunek, znaleziona ma
    najmniejszą sumę wag.
"""


class Graph:

    def __init__(self, size):
        self.size = size
        self.graph_repr = [[] for _ in range(size)]
        self.edges = []

    def add_edge(self, u, v, weight):
        """Add edge from u to v."""
        self.graph_repr[u].append([v, weight])
        self.edges.append((u, v, weight))


def path_desc_weights(graph, s, t):
    """
    Algorithms finds min weight path where weights of consecutive
    edges are in descending order.

    First, sort edges (by weight) in descending manner.
    Then, relax every edge.

    Algorithm is correct because at start, every vertex (except for s=0) in
    list has value "inf". Thus, relaxing will start at longest edge starting
    from s. In consequence, next edges have less and less length, thus we can
    be sure that length from s to v is the shortest possible path with
    descending weights of the edges.

    :param graph: representation of a graph as a list of the edges.
    :param s: starting vertex.
    :param t: final vertex.
    :returns: min distances from s to t, route - list.
    """
    n = graph.size
    parents = [None for _ in range(n)]
    dist = [float("inf") for _ in range(n)]
    dist[s] = 0

    edges = sorted(graph.edges, key=lambda x: x[2], reverse=True)
    for edge in edges:
        u = edge[0]
        v = edge[1]
        weight = edge[2]
        if dist[v] > dist[u] + weight:
            dist[v] = dist[u] + weight
            parents[v] = u

    route = []
    if not dist[t] == float("inf"):
        a = t
        while a is not None:
            route.append(a)
            a = parents[a]
    route = route[::-1]

    return dist[t], route


if __name__ == "__main__":
    G1 = Graph(5)
    G1.add_edge(0, 1, 5)
    G1.add_edge(0, 2, 4)
    G1.add_edge(1, 4, 4)
    G1.add_edge(2, 1, 2)
    G1.add_edge(2, 3, 3)
    G1.add_edge(3, 4, 1)
    print(path_desc_weights(G1, 0, 4))
    # G2 = [[0, 5, 4, 0, 0],
    #       [5, 0, 3, 0, 4],
    #       [4, 3, 0, 3, 0],
    #       [0, 0, 3, 0, 1],
    #       [0, 4, 0, 1, 0]]
    # print(path_desc_weights_matrix(G2, 0, 4))
