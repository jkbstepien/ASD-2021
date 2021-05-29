"""
Dany jest graf skierowany G = (V,E) w reprezentacji macierzowej (bez wag).
Proszę zaimplementować algorytm, który oblicza domknięcie przechodnie grafu G
(domknięcie przechodnie grafu G to taki graf H, że w H mamy krawędź z u do v
wtedy i tylko wtedy gdy w G jest ścieżka skierowana z u do v).
"""


def transitive_closure_naive_matrix(graph):
    """
    Function computes reachability matrix.
    O(V^3). Bases on Floyd-Warshall.

    :param graph: matrix representation of a graph.
    :returns: matrix.
    """
    n = len(graph)

    for i in range(n):
        for u in range(n):
            for v in range(n):
                # cases: u == v, 'i' is on path from u to v
                graph[u][v] = graph[u][v] or (graph[u][i] and graph[i][v])

    return graph


def transitive_closure(graph):
    """
    Function computes reachability matrix.
    O(V^2) for sparse graphs.

    :param graph: matrix representation of a graph.
    :returns: matrix.
    """
    n = len(graph)
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    def dfs_util(graph, matrix, s, t):
        """
        Utility function for transitive closure.
        """
        for j in graph[t]:
            # if 'j' is adjacent vertex of t, that means
            # path from s to j has been found.
            if matrix[s][j] == 0:
                matrix[s][j] = 1
                dfs_util(graph, matrix, s, j)

    for i in range(n):
        matrix[i][i] = 1
        dfs_util(graph, matrix, i, i)
        # print(matrix[i])

    return matrix


if __name__ == "__main__":
    G1 = [[0, 1, 1, 0],
          [0, 0, 1, 0],
          [1, 0, 0, 1],
          [0, 0, 0, 1]]
    # Should print: [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 1]]
    print(f"naive: {transitive_closure_naive_matrix(G1)}")

    G2 = [[1, 1, 1, 0, 0],
          [0, 0, 0, 0, 1],
          [1, 1, 0, 0, 0],
          [0, 0, 1, 0, 1],
          [0, 0, 0, 0, 1]]
    # Should print:
    # [[1, 1, 1, 0, 1], [0, 0, 0, 0, 1], [1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
    print(f"naive: {transitive_closure_naive_matrix(G2)}")

    G3 = [[1, 2], [4], [1, 0], [2, 4], []]
    # Should print: [[1, 1, 1, 0, 1], [0, 1, 0, 0, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 1]]
    print(f"adj_version: {transitive_closure(G3)}")

    G4 = [[1, 2], [2], [0, 3], []]
    # Should print: [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 1]]
    print(f"adj_version: {transitive_closure(G4)}")
