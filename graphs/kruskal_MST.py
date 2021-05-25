from union_find import make_set, find_set, union


class WeightedGraph:

    def __init__(self, size):
        self.size = size
        self.graph_repr = [[i] for i in range(size)]
        self.edges = []

    def add_edge(self, u, v, weight):
        self.graph_repr[u].append((v, weight))
        self.graph_repr[v].append((u, weight))
        self.edges.append((weight, u, v))


def kruskal_mst(graph):
    """
    Kruskal's algorithm for finding MST.
    :param graph: representation of a graph as a set of edges.
    :return: list of edges in MST where each elem is a tuple
    (distances, u, v).
    """
    n = graph.size
    graph.edges.sort()
    sets = []
    mst = []

    for i in range(n):
        sets.append(make_set(i))

    for edge in graph.edges:
        u = edge[1]
        v = edge[2]
        if find_set(sets[u]) != find_set(sets[v]):
            mst.append(edge)
            union(sets[u], sets[v])

    return mst


# Test
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
    print(kruskal_mst(G))
