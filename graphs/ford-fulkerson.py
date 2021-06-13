from queue import PriorityQueue


def bfs(graph, s, t, parent) -> bool:
    queue = PriorityQueue()
    visited = [False for _ in range(len(graph))]
    queue.put(s)
    visited[s] = True

    while not queue.empty():
        u = queue.get()
        for idx in range(len(graph[u])):
            if visited[idx] is False and graph[u][idx] > 0:
                visited[idx] = True
                parent[idx] = u
                queue.put(idx)

    return visited[t]


def ford_fulkerson(graph, source, sink) -> int:
    """
    Algorithm finds max-flow in directed graph. Uses
    Ford-Fulkerson's method with Edmond-Karp's technique
    for finding paths in graph.
    """
    n = len(graph)
    parents = [-1 for _ in range(n)]

    max_flow = 0
    while bfs(graph, source, sink, parents):
        flow_on_path = float("inf")
        s = sink
        while s != source:
            # Find minimum value on current path.
            flow_on_path = min(flow_on_path, graph[parents[s]][s])
            s = parents[s]

        max_flow += flow_on_path
        v = sink
        while v != source:
            u = parents[v]
            graph[u][v] -= flow_on_path
            graph[v][u] += flow_on_path
            v = parents[v]

    return max_flow


def main():
    graph = [
        [0, 8, 4, 0, 0, 0],
        [0, 0, 0, 12, 0, 0],
        [0, 0, 0, 2, 4, 0],
        [0, 0, 0, 0, 0, 10],
        [0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0]
    ]
    source, sink = 0, 5
    res = ford_fulkerson(graph, source, sink)
    if res == 12:
        print("good answer")


if __name__ == "__main__":
    main()
