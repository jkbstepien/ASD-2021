def dfs(G):
    n = len(G)
    visited = [False] * n
    result = []

    def dfs_visit(G, u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs_visit(G, v)
        result.append(u)

    for i in range(n):
        if not visited[i]:
            dfs_visit(G, i)

    return result


if __name__ == "__main__":
    neigh_list_1 = [[1, 3], [2, 0], [1], [4, 0], [3]]
    print(dfs(neigh_list_1))
