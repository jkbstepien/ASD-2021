def dfs_util_visit(graph, v, visited, vertexes):
    """
    Utility function for topological_sorting.
    :param graph: representation of a graph as adjacency list.
    :param v: current vertex.
    :param visited: list of visited vertexes from dfs function.
    :param vertexes: current list of processed vertexes.
    """
    visited[v] = True

    for neigh in graph[v]:
        if visited[neigh] is False:
            dfs_util_visit(graph, neigh, visited, vertexes)
    vertexes.append(v)


def topological_sorting(graph, s=0):
    """
    Modified Depth First Search algorithm for topological sorting.
    :param graph: representation of a graph as adjacency list.
    :param s: starting vertex.
    :return: list of sorted vertexes.
    """
    n = len(graph)
    visited = [False for _ in range(n)]
    vertexes = []

    dfs_util_visit(graph, s, visited, vertexes)

    return vertexes[::-1]


if __name__ == "__main__":
    G = [[1, 2, 4], [2, 3], [], [5, 6], [3], [], []]
    # Should return [0, 4, 1, 3, 6, 5, 2]
    print(topological_sorting(G))