from queue import PriorityQueue


class WeightedGraph:
    """Modified WeightedGraph class for Prim's algorithm."""

    def __init__(self, size):
        self.size = size
        self.graph_repr = [[i] for i in range(size)]

    def add_edge(self, u, v, weight):
        """
        Function populates 2D array graph_repr in form:
        [ [vertex_num, tuple, tuple,..], ... ]
        where tuple's first element is distances of edge between v and u,
        second element stands for num of vertex v/u.
        :param u: first vertex.
        :param v: second vertex.
        :param weight: distances of an edge between v and u.
        """
        self.graph_repr[u].append((weight, v))
        self.graph_repr[v].append((weight, u))


def prim_mst(graph, s=0):
    """
    Prim's algorithm for finding MST.
    :param graph: representation of a graph as a set of edges.
    :param s: starting vertex.
    :return: list of edges in MST where each elem is a tuple
    (v, u, distances).
    """
    n = graph.size
    queue = PriorityQueue()
    visited = [False for _ in range(n)]

    for vertex in range(n):
        if vertex != s:
            queue.put((float("inf"), vertex))
    queue.put((0, s))

    parents = [None for _ in range(n)]
    weights_min = [float("inf") for _ in range(n)]
    weights_min[s] = 0

    while not queue.empty():
        # get u as pair (distances, vertex num)
        v = queue.get()
        visited[v[1]] = True
        for u in graph.graph_repr[v[1]][1:]:
            if not visited[u[1]]:
                if weights_min[u[1]] > u[0]:
                    weights_min[u[1]] = u[0]
                    parents[u[1]] = v[1]
                    queue.put((u[0], u[1]))

    mst = []
    for i in range(n):
        if parents[i] is not None:
            mst.append((parents[i], i, weights_min[i]))

    return mst


if __name__ == "__main__":
    G = WeightedGraph(9)
    G.add_edge(0, 1, 1)
    G.add_edge(0, 2, 12)
    G.add_edge(1, 2, 7)
    G.add_edge(1, 3, 5)
    G.add_edge(2, 3, 6)
    G.add_edge(2, 4, 8)
    G.add_edge(3, 4, 4)
    G.add_edge(3, 5, 3000)
    G.add_edge(4, 5, 9)
    print(prim_mst(G))
