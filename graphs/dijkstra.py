from queue import PriorityQueue


class WeightedGraph:

    def __init__(self, size):
        self.size = size
        self.graph_repr = [[] for _ in range(size)]

    def add_edge(self, u, v, distance):
        """
        Function populates 2D array graph_repr in form:
        [ [tuple, tuple,..],.. ]
        where tuple's first element is num of vertex u/v,
        second element stands for weight of edge (distance)
        between u and v.
        :param u: first vertex.
        :param v: second vertex.
        :param distance: weight of an edge between u and v.
        """
        self.graph_repr[u].append((v, distance))


def dijkstra(graph, s=0):
    """
    Dijkstra's algorithm for shortest paths in
    weighted graphs. Algorith is not correct if weights
    of the edges are negative numbers.
    :param graph: representation of a graph as set of edges.
    :param s: starting vertex.
    :return: two lists: distances, parents.
    """
    n = graph.size
    queue = PriorityQueue()

    for vertex in range(n):
        queue.put((float("inf"), vertex))
    queue.put((0, s))

    parents = [None for _ in range(n)]
    distances = [float("inf") for _ in range(n)]
    distances[s] = 0

    while not queue.empty():
        v = queue.get()
        length = len(graph.graph_repr[v[1]])
        for i in range(length):
            u = graph.graph_repr[v[1]][i]
            if distances[u[0]] > distances[v[1]] + u[1]:
                distances[u[0]] = distances[v[1]] + u[1]
                parents[u[0]] = v[1]
                queue.put((distances[u[0]], u[0]))

    return distances, parents


if __name__ == "__main__":
    G = WeightedGraph(7)
    G.add_edge(0, 1, 1)
    G.add_edge(0, 2, 5)
    G.add_edge(1, 2, 2)
    G.add_edge(1, 3, 8)
    G.add_edge(1, 4, 7)
    G.add_edge(2, 3, 3)
    G.add_edge(3, 4, 1)
    # Should print ([0, 1, 3, 6, 7, inf, inf], [None, 0, 1, 2, 3, None, None])
    print(dijkstra(G))
