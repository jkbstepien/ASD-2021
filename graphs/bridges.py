def bridges(graph) -> list:
    """
    Function searches for bridges in undirected graph.
    """
    n = len(graph)
    time = 0
    visited = [False for _ in range(n)]
    parents = [None for _ in range(n)]
    vertex_visit_time = [None for _ in range(n)]
    low = [None for _ in range(n)]

    def mod_dfs_visit(u):
        nonlocal time
        time += 1
        vertex_visit_time[u] = time
        low[u] = time
        visited[u] = True

        for v in range(len(graph[u])):
            neigh = graph[u][v]
            if not visited[neigh]:
                visited[neigh] = True
                parents[neigh] = u
                mod_dfs_visit(neigh)
                low[u] = min(low[u], low[neigh])
            elif visited[neigh] and parents[u] != neigh:
                low[u] = min(low[u], vertex_visit_time[neigh])

    for v in range(n):
        if not visited[graph[v][0]]:
            mod_dfs_visit(graph[v][0])

    bridges_lst = []
    for i in range(n):
        if vertex_visit_time[i] == low[i] and parents[i] is not None:
            # We've found a bridge.
            bridges_lst.append((parents[i], i))

    return bridges_lst


def main():
    G = [
        [1, 6],
        [0, 2],
        [1, 3, 6],
        [2, 4, 5],
        [3, 5],
        [3, 4],
        [0, 2, 7],
        [6]
    ]
    print(bridges(G))


if __name__ == "__main__":
    main()
