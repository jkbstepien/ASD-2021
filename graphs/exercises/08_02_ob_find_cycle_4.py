def bfs(G):
    n = len(G)

    for i in range(n):
        queue = [i]
        distances = [-1] * n
        distances[i] = 0
        visited = [False] * n
        parent = [None] * n

        while queue:
            v = queue.pop(0)
            for j in range(n):
                if G[v][j] == 1 and not visited[j]:
                    parent[j] = v
                    visited[j] = True
                    distances[j] = distances[v] + 1
                    queue.append(j)
                elif (G[v][j] == 1 and
                      parent[v] != j and
                      distances[v] + 1 == distances[j] == 2):
                    return True

    return False


if __name__ == "__main__":
    graph = [[0, 1, 0, 1],
             [1, 0, 1, 1],
             [0, 1, 0, 1],
             [1, 1, 1, 0]]
    print(bfs(graph))
