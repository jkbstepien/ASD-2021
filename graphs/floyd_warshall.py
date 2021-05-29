def floyd_warshall(graph):
    """
    Floyd-Warshall algorithm for shortest paths between
    two specified vertices.
    :param graph: matrix representation of a graph.
    :returns: two lists: distances, parents.
    """
    n = len(graph)
    dist = [[0] * n for _ in range(n)]
    parents = [[float("inf")] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j]:
                dist[i][j] = graph[i][j]
            else:
                dist[i][j] = float("inf")

    for i in range(n):
        for j in range(n):
            for k in range(n):
                prev_value = dist[j][i] + dist[i][k]
                if dist[j][k] > prev_value:
                    dist[j][k] = prev_value
                    parents[j][k] = i

    return dist, parents


if __name__ == "__main__":
    G1 = [[0, 1, 5, 0, 0],
          [1, 0, 2, 8, 7],
          [5, 2, 0, 3, 0],
          [0, 8, 3, 0, 1],
          [0, 7, 0, 1, 0]]
    print(floyd_warshall(G1))
