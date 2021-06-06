"""
Zad. (spójność krawędziowa)

Dany jest graf nieskierowany G = (V,E). Mówimy, że spójność krawędziowa wynosi k
jeżeli usunięcie pewnych k krawędzi powoduje, że G jest niespójny, ale usunięcie
dowolnych k-1 krawędzi nie rozspójnia go. Proszę podać algorytm, który oblicza spójność
krawędziową grafu.

Algorytm:
    -> Zakładamy, że każda z krawędzi ma przepustowość 1.
    -> Następnie z każdego wierzchołka v znajdujemy przepływ do do każdego innego (|V|-1 * max-flow).
        -> Trzeba wykorzystać algorytm max-flow dla grafu nieskierowanego.
    -> Nasza spójność krawędziowa to najmniejszy z maksymalnych przepływów.
        -> Usunięcie dokładnie tylu krawędzi powoduje rozspójnienie grafu.
"""