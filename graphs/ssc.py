def dfs(graph):
    n = len(graph)
    visited = [False for _ in range(n)]
    finish_times = [None for _ in range(n)]
    time = 0

    def dfs_visit(vertex):
        nonlocal time
        visited[vertex] = True

        for i in range(len(graph[vertex])):
            neigh = graph[vertex][i]
            if not visited[neigh]:
                visited[neigh] = True
                dfs_visit(neigh)

        time += 1
        finish_times[vertex] = (vertex, time)

    for u in range(n):
        if graph[u]:
            if not visited[graph[u][0]]:
                dfs_visit(graph[u][0])

    return finish_times


def reverse_edges(graph) -> list:
    """
    Function reverses edges in given graph.
    """
    n = len(graph)
    reversed_edges = [[] for _ in range(n)]

    for u in range(n):
        for v in graph[u]:
            reversed_edges[v].append(u)

    return reversed_edges


def ssc(graph) -> (int, list):
    """
    Function searches for Strongly Connected Components
    in a graph.
    """
    n = len(graph)
    times = dfs(graph)
    times.sort(key=lambda x: x[1], reverse=True)
    new_graph = reverse_edges(graph)

    def visit_vertex(u):
        components[counter].append(u)
        visited[u] = True

        for v in range(len(new_graph[u])):
            neigh = new_graph[u][v]
            if not visited[neigh]:
                visited[neigh] = True
                visit_vertex(neigh)

    visited = [False for _ in range(n)]
    components = []
    counter = 0
    for time in times:
        vertex = time[0]
        if not visited[vertex]:
            components.append([])
            visit_vertex(vertex)
            counter += 1

    return counter, components


def main():
    G1 = [
        [1, 4],  # 0
        [2, 3],  # 1
        [0, 7],  # 2
        [4],     # 3
        [5],     # 4
        [3, 6],  # 5
        [3],     # 6
        [8],     # 7
        [9],     # 8
        [10],    # 9
        [6, 7],  # 10
    ]
    G2 = [
        [1, 2],
        [3],
        [],
        [0]
    ]
    print(dfs(G1))
    print(G1)
    print(reverse_edges(G1))
    print(ssc(G1))


if __name__ == "__main__":
    main()
