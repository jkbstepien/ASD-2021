def bellman_ford(graph, s=0):
    """
    Bellman-Ford algorithm for shortest paths in directed
    weighted graphs. Weight of an edge can be negative value.
    :param graph: matrix representation of a graph.
    :param s: starting vertex.
    :returns: lists of distances and parents.
    """
    n = len(graph)
    distances = [float("inf") for _ in range(n)]
    parents = [float("inf") for _ in range(n)]
    distances[s] = 0

    for i in range(n - 1):
        for u in range(n):
            for v in range(n):
                if distances[v] > distances[u] + graph[u][v]:
                    distances[v] = distances[u] + graph[u][v]
                    parents[v] = u

    for u in range(n):
        for v in range(n):
            if distances[v] > distances[u] + graph[u][v]:
                msg = "Negative cycle."
                return msg

    return distances, parents


if __name__ == "__main__":
    inf = float("inf")

    G1 = [[inf, 1, 5, inf, inf],
          [1, inf, 2, 8, 7],
          [5, 2, inf, 3, inf],
          [inf, 8, 3, inf, 1],
          [inf, 7, inf, 1, inf]]

    G2 = [[inf, 1, 5, inf, inf],
          [1, inf, 2, 8, 7],
          [5, 2, inf, 3, inf],
          [inf, 8, 3, inf, -10],
          [inf, 7, inf, -10, inf]]

    G3 = [[inf, 1, 5, inf, inf],
          [1, inf, 2, 8, -1],
          [5, 2, inf, 3, inf],
          [inf, 8, 3, inf, -3],
          [inf, inf, inf, inf, inf]]

    # Should print:
    #   ([0, 1, 3, 6, 7], [None, 0, 1, 2, 3])
    #   Negative cycle.
    #   ([0, 1, 3, 6, 0], [None, 0, 1, 2, 1])
    print(bellman_ford(G1))
    print(bellman_ford(G2))
    print(bellman_ford(G3))
