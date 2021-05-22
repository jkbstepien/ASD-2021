def cycle_util(graph, v, visited, parent):
    """
    Utility function for cycle.
    :param graph: representation of a graph as adjacency list.
    :param v: current vertex.
    :param visited: list of visited vertexes.
    :param parent: list of vertexes' parents.
    :return: boolean value for cycle function.
    """
    visited[v] = True

    for u in graph[v]:
        if not visited[u]:
            parent[u] = v
            cycle_util(graph, u, visited, parent)
        elif visited[u] and parent[u] != v:
            return True

    return False


def cycle(graph, s=0):
    """
    Function determines whether graph has a cycle.
    :param graph: graph as adjacency list.
    :param s: starting vertex.
    :return: boolean value.
    """
    n = len(graph)
    visited = [False] * n
    parent = [False] * n

    return cycle_util(graph, s, visited, parent)


if __name__ == "__main__":
    G = [[1, 3], [2, 0], [3, 1], [4, 0], [3]]
    G2 = [[1, 3], [2, 0], [1], [4, 0], [3]]
    G3 = [[1, 2], [2, 0], [0, 1]]
    print(cycle(G))
    print(cycle(G2))
    print(cycle(G3))
