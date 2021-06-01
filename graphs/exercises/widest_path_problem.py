"""
Offline excercise nr 10.
"""
from queue import PriorityQueue


def f(route, parents, u):
    """Store vertices of a route in list."""
    if parents[u] is not None:
        f(route, parents, parents[u])
    route.append(u)


def widest_path(graph, s, t):
    n = len(graph)
    queue = PriorityQueue()
    parents = [None for _ in range(n)]
    width = [float("-inf") for _ in range(n)]

    width[s] = float("inf")
    queue.put((0, 0, s))

    while not queue.empty():
        _, _, u = queue.get()
        if not graph[u] == []:
            for v, weight in graph[u]:
                new_dist = max(width[v], min(width[u], weight))
                if width[v] < new_dist:
                    width[v] = new_dist
                    parents[v] = u
                    queue.put((new_dist, -weight, v))

    route = []
    f(route, parents, t)

    return width[t], route


if __name__ == "__main__":
    G1 = [
        [(1, 4), (2, 3)],
        [(3, 2)],
        [(3, 5)],
        []
    ]
    # Should print: (3, [0, 2, 3])
    print(widest_path(G1, 0, 3))

    G2 = [
        [(1, 5), (2, 4)],
        [(4, 4)],
        [(1, 2), (3, 3)],
        [(4, 1)],
        []
    ]
    # Should print: (4, [0, 1, 4])
    print(widest_path(G2, 0, 4))

    G3 = [
        [(1, 10), (2, 11), (3, 5)],
        [(2, 5)],
        [(3, 7), (5, 3), (4, 6)],
        [(4, 7), (5, 4)],
        [(5, 5)],
        []
    ]
    # Should print: (5, [1, 2, 4, 5])
    print(widest_path(G3, 1, 5))