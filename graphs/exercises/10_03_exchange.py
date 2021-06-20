"""
Dana jest tabela kursów walut. Dla każdych dwóch walut x oraz y wpis K[x][y]
oznacza ile trzeba zapłacić waluty x żeby otrzymać jednostkę waluty y.
Proszę zaproponować algorytm, który sprawdza czy istnieje taka waluta z, że
za jednostkę z można uzyskać więcej niż jednostkę z przez serię wymian walut.

Algorytm:
    Każda waluta to wierzchołek, a waga krawędzi to kurs wymiany waluty x na walutę y.
    Jeżeli iloczyn kursów na naszej ścieżce będzie większy od 1 to znaczy, że zarobiliśmy
        na transakcji.
    Szukamy odpowiedniego cyklu, którego iloczyn kursów (k1, k2,..., kn) jest większy od 1:
        Korzystamy z własności działań na logarytmach:
        log(x*y) = log(x) + log(y)
        log(k1) + log(k2) + ... + log(kn) > 0
        -log(k1) - log(k2) - ... - log(kn) < 0
    Korzystamy z algorytmu Bellmana-Forda.
    Po przeprowadzeniu relaksacji sprawdzamy warunek czy mimo naszych zmian istnieje
        droga o mniejszej wadze, a to jest możliwe tylko wtedy gdy istnieje cykl ujemny.
    Zatem jeżeli znajdziemy ujemny cykl, to wiemy, że istnieje taki szereg wymian, który
        pozwoli nam uzyskać więcej niż mieliśmy danej waluty.
"""
import math


def bellman_ford(graph, s=0):
    """
    Bellman-Ford algorithm for shortest paths in directed
    weighted graphs. Weight of an edge can be negative value.
    :param graph: matrix representation of a graph.
    :param s: starting vertex.
    :returns: lists of distances and parents.
    """
    n = len(graph)
    distances = [float("inf") for _ in range(n)]
    parents = [float("inf") for _ in range(n)]
    distances[s] = 0

    for i in range(n - 1):
        for u in range(n):
            for v in range(n):
                if distances[v] > distances[u] + graph[u][v]:
                    distances[v] = distances[u] + graph[u][v]
                    parents[v] = u

    end = 0
    for u in range(n):
        for v in range(n):
            if distances[v] > distances[u] + graph[u][v]:
                return True

    return False


def exchange(graph):
    n = len(graph)

    for i in range(n):
        for j in range(n):
            if graph[i][j] != float("inf"):
                graph[i][j] = -math.log(graph[i][j], 10)

    return bellman_ford(graph)


def main():
    # Tests.
    # Order of currencies: PLN, EUR, USD, GBP.
    inf = float("inf")
    exchange_rates1 = [
        [inf, 0.22, 0.26, 0.19],
        [4.55, inf, 1.19, 0.85],
        [3.83, 0.84, inf, 0.72],
        [5.29, 1.16, 1.38, inf]
    ]
    exchange_rates2 = [
        [inf, 5, 2],
        [2.5, inf, 2],
        [1, 0.5, inf]
    ]
    exchange_rates3 = [
        [inf, 0.9],
        [0.1, inf]
    ]
    # Should be True, True, False
    print(exchange(exchange_rates1))
    print(exchange(exchange_rates2))
    print(exchange(exchange_rates3))


if __name__ == "__main__":
    main()
