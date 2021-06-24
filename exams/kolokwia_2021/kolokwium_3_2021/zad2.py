"""
Jakub Stępień

Złożoność obliczeniowa: liniowa względem liczby wierzchołków bo raz wchodzimy do danego wierzchołka. O(V)
Algorytm:
    W funkcji get_cut_value schodzimy rekurencyjnie od korzenia w kierunku liści.
    Dla każdego node'a sprawdzamy, czy bardziej opłaca nam się wyciąć ten node, czy node'y z poddrzew jego dzieci.
    Porównujemy, czy suma optymalnych wycięć w podrzewach dzieci jest większa od naszej wartości. Jeśli jest większa, to
    bardziej opłaca nam się wyciąć aktualny node, jeśli mniejsza to bardziej opłaca się dokonać optymalnych wycięć
    w poddrzewach dzieci. Optymalna suma wycięć w podrzewie dziecka to wartość funkcji get_cut_value dla tego dziecka.
    Definiujemy, że wartość optymalnego wycięcia dla poddrzewa zawierającego sam liść to nieskończoność.
"""

from zad2testy import runtests


class BNode:
    def __init__( self, value ):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


def get_cut_value(node):
    if node.left is None and node.right is None:
        return float('inf')

    children_minimal_cut = 0
    if node.left is not None:
        children_minimal_cut += get_cut_value(node.left)
    if node.right is not None:
        children_minimal_cut += get_cut_value(node.right)
    return min(children_minimal_cut, node.value)


def cutthetree(T):
    """tu prosze wpisac wlasna implementacje"""
    sum = 0
    if T.left is not None:
        sum += get_cut_value(T.left)
    if T.right is not None:
        sum += get_cut_value(T.right)
    return sum


runtests(cutthetree)
