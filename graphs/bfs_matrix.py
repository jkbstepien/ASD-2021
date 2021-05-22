from queue import Queue


def bfs(graph, s):
    """
    Breadth First Seach Algorithm. Prints vertexes in visited order.
    :param graph: matrix representation of a graph.
    :param s: starting vertex.
    """
    queue = Queue()
    n = len(graph)
    visited = [False for _ in range(n)]

    visited[s] = True
    queue.put(s)

    while not queue.empty():
        u = queue.get()
        print(u, end=" ")
        for neigh in range(n):
            if visited[neigh] is False and graph[u][neigh] == 1:
                visited[neigh] = True
                queue.put(neigh)


if __name__ == "__main__":
    G = [[0, 1, 0, 1, 0],
         [1, 0, 1, 0, 0],
         [0, 1, 0, 1, 0],
         [1, 0, 1, 0, 1],
         [0, 0, 0, 1, 0]]
    bfs(G, 0)
