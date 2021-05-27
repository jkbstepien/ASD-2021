class Graph:

    def __init__(self, V):
        self.V = V
        self.graph = [[0 for column in range(V)] for row in range(V)]

    def is_bipartite(self, src):

        colors = [-1] * self.V
        colors[src] = 1

        queue = [src]
        while queue:
            u = queue.pop()
            # Return false if there is a self-loop
            if self.graph[u][u] == 1:
                return False

            for v in range(self.V):
                if self.graph[u][v] == 1 and colors[v] == -1:
                    colors[v] = 1 - colors[u]
                    queue.append(v)
                elif self.graph[u][v] == 1 and colors[v] == colors[u]:
                    return False

        return True


if __name__ == "__main__":
    g = Graph(4)
    g.graph = [[0, 1, 0, 1],
               [1, 0, 1, 0],
               [0, 1, 0, 1],
               [1, 0, 1, 0]]

    print(g.is_bipartite(0))
