"""
Dany jest graf G = (V,E) oraz wierzchołki s i t. Proszę zaproponować algorytm
znajdujący maksymalną liczbę rozłącznych (wierzchołkowo) ścieżek między s i t.

Algorytm:
    -> Chcemy sprowadzić problem do szukania maksymalnego przepływu w grafie.
    -> Musimy sobie zagwarantować, że do każdego wierzchołka wejdziemy i wyjdziemy
        tylko raz.
    -> Każdy wierzchołek rozdzielamy na dwa (u, v):
        -> Krawędzie, które wchodziły do danego wierzchołka przyłączamy do u.
        -> Krawędzie, które wychodziły z danego wierzchołka przyłączamy do v.
    -> W przypadku gdy puścimy przepływ przez krawędź łączącą rozdzielony wierzchołek
        mamy pewność, że tamtędy żadna ścieżka już nie popłynie ponieważ przepustowość
        każdej krawędzi to 1.
    -> Zakładamy, że każda krawędź ma przepustowość 1.
    -> Znajdujemy maksymalny przepływ między s i t => jest to liczba rozłącznych
        wierzchołkowo ścieżek.
"""