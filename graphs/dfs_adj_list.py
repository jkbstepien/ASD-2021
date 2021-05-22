def dfs_util_visit(graph, v, visited):
    """
    Utility function for DFS algorithm.
    :param graph: representation of a graph as adjacency list.
    :param v: current vertex.
    :param visited: list of visited vertexes from dfs function.
    """
    visited[v] = True
    print(v, end=" ")

    for neigh in graph[v]:
        if visited[neigh] is False:
            dfs_util_visit(graph, neigh, visited)


def dfs(graph, s):
    """
    Depth First Search algorithm. Prints vertexes in visited order.
    :param graph: representation of a graph as adjacency list.
    :param s: starting vertex.
    """
    n = len(graph)
    visited = [False for _ in range(n)]

    dfs_util_visit(graph, s, visited)


adj_list_1 = [[1, 2, 7], [3, 4, 0], [5, 6, 0], [1], [1], [2], [2], [0]]
adj_list_2 = [[1, 2, 3], [2, 0], [4, 1, 0], [2, 0], [2]]

dfs(adj_list_1, 0)
print()
dfs(adj_list_2, 0)
