"""
Jakub Stępień

Złożoność obliczeniowa:
Algorytm:
    Wyznaczamy odległości między każdą parą wierzchołków, za pomocą alogrytmu
    Tworzymy nowy graf przy użyciu algorytmu Floyda-Warshalla. Otrzymujemy minimalne
    odległości między każdą parą wierzchołków.
    Do stworzonego przez nas grafu dodajemy super-źródło i super-ujście.
    Wszystkie niebieskie wierzchołki łączymy z super-źródłem, zaś wszystkie zielone - z super-ujściem.
    Mamy dwa zbiory wierzchołków: niebieskie i zielone. Z tych dwóch zbiorów
    konstruujemy graf dwudzielny.
    Zakładamy, że wszystkie krawędzie w grafie mają wagę 1.
    Każdy niebieski wierzchołek łączymy z zielonym wtedy i tylko wtedy gdy odległość między nimi
    jest nie mniejsza niż dane w zadaniu 'D'.
    Stosujemy algorytm Edmonds'a-Karpa z super-źródła do super-ujścia. Wynikiem jest maksymalny przepływ
    między s i t - jest to również maksymalna liczba par wierzchołków spełniających warunki zadania.
"""

from zad3testy import runtests
from zad3EK    import edmonds_karp


def floyd_warshall(graph):
    """
    Floyd-Warshall algorithm for shortest paths between
    two specified vertices.
    :param graph: matrix representation of a graph.
    :returns: two lists: distances, parents.
    """
    n = len(graph)
    dist = [[0] * n for _ in range(n)]
    parents = [[float("inf")] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j]:
                dist[i][j] = graph[i][j]
            else:
                dist[i][j] = float("inf")

    for i in range(n):
        for j in range(n):
            for k in range(n):
                prev_value = dist[j][i] + dist[i][k]
                if dist[j][k] > prev_value:
                    dist[j][k] = prev_value
                    parents[j][k] = i

    return dist, parents


def BlueAndGreen(T, K, D):
    """
    Zakladamy, ze gdy nie ma sciezki, to ma ona dlugosc nieskonczonosc czyli jest nie mniejsza niz d.
    """
    n = len(K)
    edm_kar_graph = [[0] * (n+2) for _ in range(n+2)]
    s = n
    t = n + 1
    for i in range(n):
        if K[i] == 'B': # If it is a blue vertex -> then add an edge from s to the vertex
            edm_kar_graph[s][i] = 1
        else: # if it is a green vertex, then add an edge from the vertex to t
            edm_kar_graph[i][t] = 1
    distances, _ = floyd_warshall(T)
    for i in range(len(K)):
        if K[i] == 'B': # if blue vertex
            for j in range(len(K)):
                if K[j] == 'G': # if green vertex
                    if distances[i][j] >= D: # If distance between blue and green is >= D
                        edm_kar_graph[i][j] = 1 # Add an edge from blue to green

    return edmonds_karp(edm_kar_graph, s, t)


runtests( BlueAndGreen ) 
