from queue import Queue


def bfs(graph, s):
    """
    Breadth First Seach algorithm. Prints vertexes in visited order.
    :param graph: representation of a graph as adjacency list.
    :param s: starting vertex.
    """
    visited = []
    queue = Queue()
    visited.append(s)
    queue.put(s)

    i = 0
    while not queue.empty():
        u = queue.get()
        print(u, end=" ")

        for neigh in graph[i]:
            if neigh not in visited:
                visited.append(neigh)
                queue.put(neigh)
        i += 1


if __name__ == "__main__":
    neigh_list = [[1, 2, 7],
                  [3, 4, 0],
                  [5, 6, 0],
                  [1],
                  [1],
                  [2],
                  [2],
                  [0]]
    bfs(neigh_list, 0)
