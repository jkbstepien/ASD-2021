from copy import deepcopy


def euler(G):
    """
    Function checks whether graph G has an Euler Cycle.
    :param G: Matrix representation of a graph G.
    :return: List of consecutive vertexes in cycle.
    """
    route = []

    def dfs_visit(u):
        """
        DFS visit algorithm. Every visited edge is
        marked as 'x'.
        :param u: A vertex in graph G.
        """

        for v in range(len(G)):
            # Check if edge exist and is not visited.
            if G[u][v] == 1:
                G[u][v] = G[v][u] = 'x'
                dfs_visit(v)
        route.append(u)

    dfs_visit(0)
    print(f"route: {route}")
    return route


# Tests for function euler(G).
# We assume that graph has Eulerian cycle.
if __name__ == "__main__":
    G = [[0, 1, 1, 0, 0, 0],
         [1, 0, 1, 1, 0, 1],
         [1, 1, 0, 0, 1, 1],
         [0, 1, 0, 0, 0, 1],
         [0, 0, 1, 0, 0, 1],
         [0, 1, 1, 1, 1, 0]]

    GG = deepcopy(G)
    cycle = euler(G)

    if cycle is None:
        print("Error (1)!")
        exit(0)

    u = cycle[0]
    for v in cycle[1:]:
        if not GG[u][v]:
            print("Error (2)!")
            exit(0)
        GG[u][v] = False
        GG[v][u] = False
        u = v

    for i in range(len(GG)):
        for j in range(len(GG)):
            if GG[i][j]:
                print("Error (3)!")
                exit(0)

    print("OK")
