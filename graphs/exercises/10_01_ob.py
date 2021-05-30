"""
Dany jest graf nieskierowany G = (V,E) z ważonymi krawędziami (w: E -> N).
Proszę zaproponować jak najszybszy algorytm, który znajduje ścieżkę z danego
wierzchołka s do danego wierzchołka v, taką że:
    1. Każda kolejna krawędź ma mniejszą wagę niż poprzednia.
    2. Spośród ścieżek spełniających powyższy warunek, znaleziona ma
    najmniejszą sumę wag.
"""
from queue import PriorityQueue


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


def path_desc_weights_adj(graph, s, t):
    """
    Algorithms finds min weight path where weights of consecutive
    edges are in descending order.
    Adjacency list version.

    :param graph: graph as a adjacency list.
    :param s: starting vertex.
    :param t: final vertex.
    :returns: min distance from s to t, route - list.
    """
    n = len(graph)
    queue = PriorityQueue()
    parents = [None for _ in range(n)]
    dist = [float("inf") for _ in range(n)]

    dist[s] = 0
    queue.put((0, 0, s))

    while not queue.empty():
        prev_w, _, u = queue.get()
        if not graph[u] == []:
            for v, weight in graph[u]:
                if parents[u] is None:
                    new_dist = dist[u] + weight
                    if dist[v] > new_dist:
                        dist[v] = new_dist
                        parents[v] = u
                        queue.put((new_dist, -weight, v))
                elif prev_w > weight:
                    new_dist = dist[u] + weight
                    if dist[v] > new_dist:
                        dist[v] = new_dist
                        parents[v] = u
                        queue.put((new_dist, -weight, v))

    # Find path with min sum of weights.
    route = []
    get_route(route, parents, t)

    return dist[t], route


def relax(cost, parent, v, u, cvu):
    """Relax function for path_desc_weights."""
    if cost[u] > cost[v] + cvu:
        cost[u] = cost[v] + cvu
        parent[u] = v


def get_route(route, parents, u):
    """Store vertices of a route in list."""
    if parents[u] is not None:
        get_route(route, parents, parents[u])
    route.append(u)


def path_desc_weights_matrix(graph, s, t):
    """
    Matrix version of path_desc_weights.

    :param graph: matrix representation of a graph.
    :param s: starting vertex.
    :param t: final vertex.
    :returns: min distance from s to t, route - list.
    """
    n = len(graph)
    queue = PriorityQueue()
    parents = [None for _ in range(n)]
    dist = [float("inf") for _ in range(n)]

    dist[s] = 0
    queue.put((0, 0, s))

    while not queue.empty():
        _, _, v = queue.get()
        for i in range(n):
            # Relax only if certain edge is first to consider,
            if graph[v][i] and parents[v] is None:
                relax(dist, parents, v, i, graph[v][i])
                queue.put((dist[i], -graph[v][i], i))
            # or it's parent has more weight.
            elif graph[v][i] and graph[parents[v]][v] > graph[v][i]:
                relax(dist, parents, v, i, graph[v][i])
                queue.put((dist[i], -graph[v][i], i))

    # Find path with min sum of weights.
    route = []
    get_route(route, parents, t)

    return dist[t], route


if __name__ == "__main__":
    # In each test you should get: (8, [0, 2, 3, 4])
    # List of edges.
    G1 = Graph(5)
    G1.add_edge(0, 1, 5)
    G1.add_edge(0, 2, 4)
    G1.add_edge(1, 4, 4)
    G1.add_edge(2, 1, 2)
    G1.add_edge(2, 3, 3)
    G1.add_edge(3, 4, 1)
    print(path_desc_weights(G1, 0, 4))

    # Adjacency list.
    G2 = [
        [(1, 5), (2, 4)],
        [(4, 4)],
        [(1, 2), (3, 3)],
        [(4, 1)],
        []
    ]
    print(path_desc_weights_adj(G2, 0, 4))

    # Matrix representation.
    G3 = [
        [0, 5, 4, 0, 0],
        [0, 0, 0, 0, 4],
        [0, 2, 0, 3, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0]
    ]
    print(path_desc_weights_matrix(G3, 0, 4))
