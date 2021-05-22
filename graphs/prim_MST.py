from queue import PriorityQueue


class WeightedGraph:

    def __init__(self, size):
        self.size = size
        self.graph_repr = [[i] for i in range(size)]

    def add_edge(self, u, v, weight):
        self.graph_repr[u].append((v, weight))
        self.graph_repr[v].append((u, weight))


def prim_mst(graph, s=0):
    """
    Prim's algorithm for finding MST.
    :param graph: representation of a graph as a set of edges.
    :param s: starting vertex.
    :return: list of edges in MST where each elem is a tuple
    (u, v, weight).
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
        v = queue.get()
        visited[v[1]] = True
        for u in graph.graph_repr[v[1]][1:]:
            if not visited[u[0]]:
                if weights_min[u[0]] > u[1]:
                    weights_min[u[0]] = u[1]
                    parents[u[0]] = v[1]
                    queue.put((u[1], u[0]))

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
