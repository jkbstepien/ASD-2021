from queue import PriorityQueue


def dijkstra_adj(graph, s=0):
    n = len(graph)
    queue = PriorityQueue()
    parents = [None for _ in range(n)]
    dist = [float("inf") for _ in range(n)]

    dist[s] = 0
    queue.put((0, 0, s))

    while not queue.empty():
        _, _, u = queue.get()
        if not graph[u] == []:
            for v, weight in graph[u]:
                new_dist = dist[u] + weight
                if dist[v] > new_dist:
                    dist[v] = new_dist
                    parents[v] = u
                    queue.put((new_dist, -weight, v))

    return dist, parents


def relax(dst, parent, infinity, v, u, weight_v_u):
    """Utility function for dijkstra."""

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


def dijkstra_matrix(graph, s=0):
    """
    Dijkstra's algorithm for shortest paths in
    weighted graphs. Algorithm is not correct if weights
    of the edges are negative numbers.
    :param graph: matrix representation of a graph.
    :param s: starting vertex
    :return: two lists: distances, parents.
    """
    n = len(graph)
    queue = PriorityQueue()

    infinity = [True for _ in range(n)]
    parents = [None for _ in range(n)]
    distances = [float("inf") for _ in range(n)]

    infinity[s] = False
    distances[s] = 0
    queue.put((0, s))

    while not queue.empty():
        _, v = queue.get()
        for u in range(n):
            if graph[v][u] > 0:
                if relax(distances, parents, infinity, v, u, graph[v][u]):
                    queue.put((distances[u], u))

    return distances, parents


if __name__ == "__main__":
    G1 = [
        [0, 1, 5, 0, 0],
        [1, 0, 2, 8, 7],
        [5, 2, 0, 3, 0],
        [0, 8, 3, 0, 1],
        [0, 7, 0, 1, 0]
    ]
    G2 = [
        [-1, 2, -1, -1, 1],
        [2, -1, 4, 1, -1],
        [-1, 4, -1, 5, -1],
        [-1, 1, 5, -1, 3],
        [1, -1, -1, 3, -1]
    ]
    G3 = [
        [-1, 2, -1, -1, 1],
        [2, -1, -1, 1, -1],
        [-1, -1, -1, 5, -1],
        [-1, 1, 5, -1, 3],
        [1, -1, -1, 3, -1]
    ]
    G4 = [
        [0, 5, 4, 0, 0],
        [0, 0, 0, 0, 4],
        [0, 2, 0, 3, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0]
    ]
    G5 = [
        [(1, 5), (2, 4)],
        [(4, 4)],
        [(1, 2), (3, 3)],
        [(4, 1)],
        []
    ]
    # Should print ([0, 1, 3, 6, 7], [None, 0, 1, 2, 3])
    print(dijkstra_matrix(G1))
    # Should print ([0, 2, 6, 3, 1], [None, 0, 1, 1, 0])
    print(dijkstra_matrix(G2))
    # Should print ([0, 2, 8, 3, 1], [None, 0, 3, 1, 0])
    print(dijkstra_matrix(G3))
    # Should print ([0, 5, 4, 7, 8], [None, 0, 0, 2, 3])
    print(dijkstra_matrix(G4))
    # Should print ([0, 5, 4, 7, 8], [None, 0, 0, 2, 3])
    print(dijkstra_adj(G5))
