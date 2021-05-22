def cycle_util(graph, v, visited, parent):
    """
    Utility function for cycle.
    :param graph: matrix representation of a graph.
    :param v: current vertex.
    :param visited: list of visited vertexes.
    :param parent: list of vertexes' parents.
    :return: boolean value for cycle function.
    """
    n = len(graph)
    visited[v] = True

    for u in range(n):
        if graph[v][u] == 1:
            if not visited[u]:
                parent[u] = v
                return cycle_util(graph, u, visited, parent)
            else:
                if u != parent[v]:
                    return True

    return False


def cycle(graph):
    """
    Function for determining whether graph has a cycle.
    :param graph: matrix representation of a graph.
    :return: boolean value whether cycle has been found or not.
    """
    n = len(graph)
    visited = [False] * n
    parent = [-1] * n

    return cycle_util(graph, 0, visited, parent)


if __name__ == "__main__":
    G1 = [[0, 1, 0, 1, 0],
          [1, 0, 1, 0, 0],
          [0, 1, 0, 1, 0],
          [1, 0, 1, 0, 1],
          [0, 0, 0, 1, 0]]
    G2 = [[0, 1, 0, 1, 0],
          [1, 0, 1, 0, 0],
          [0, 1, 0, 0, 0],
          [1, 0, 0, 0, 1],
          [0, 0, 0, 1, 0]]
    # Should print True, False
    print(f"{cycle(G1)}, {cycle(G2)}")
