def dfs_util_visit(graph, v, visited):
    """
    Utility function for DFS algorithm.
    :param graph: matrix representation of a graph.
    :param v: current vertex.
    :param visited: list of visited vertexes from dfs function.
    """
    n = len(graph)
    visited[v] = True
    print(v, end=" ")

    for neigh in range(n):
        if visited[neigh] is False and graph[v][neigh] == 1:
            dfs_util_visit(graph, neigh, visited)


def dfs(graph, s):
    """
    Depth First Search algorithm. Prints vertexes in visited order.
    :param graph: matrix representation of a graph.
    :param s: starting vertex.
    """
    n = len(graph)
    visited = [False for _ in range(n)]

    dfs_util_visit(graph, s, visited)


if __name__ == "__main__":
    G = [[0, 1, 0, 0, 1],
         [1, 0, 1, 0, 0],
         [0, 1, 0, 1, 0],
         [0, 0, 1, 0, 0],
         [1, 0, 0, 0, 0]]
    dfs(G, 0)
