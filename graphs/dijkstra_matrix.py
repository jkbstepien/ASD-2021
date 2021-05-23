from queue import PriorityQueue


def dijkstra(graph, s=0):
    """
    Dijkstra's algorithm for shortest paths in
    weighted graphs. Algorith is not correct if weights
    of the edges are negative numbers.
    :param graph: matrix representation of a graph.
    :param s: starting vertex
    :return: two lists: distances, parents.
    """
    n = len(graph)
    queue = PriorityQueue()

    for vertex in range(n):
        queue.put((float("inf"), vertex))
    queue.put((0, s))

    parents = [None for _ in range(n)]
    distances = [float("inf") for _ in range(n)]
    distances[s] = 0

    while not queue.empty():
        _, v = queue.get()
        for u in range(n):
            # If there is non zero matrix cell.
            if graph[v][u]:
                if distances[v] > distances[u] + graph[v][u]:
                    distances[v] = distances[u] + graph[v][u]
                    parents[v] = u
                    queue.put((distances[u], u))

    return distances, parents


if __name__ == "__main__":
    G = [[0, 1, 5, 0, 0],
         [1, 0, 2, 8, 7],
         [5, 2, 0, 3, 0],
         [0, 8, 3, 0, 1],
         [0, 7, 0, 1, 0]]
    # Should print ([0, 1, 3, 6, 7], [None, 0, 1, 2, 3])
    print(dijkstra(G))
