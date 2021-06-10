"""
Proszę podać algorytm, który mając na wejściu drzewo oblicza skojarzenie
o maksymalnej liczności.

Algorytm:
    -> Każde drzewo jest grafem dwudzielnym.
    -> Możemy zatem zastosować algorytm do znajdywania maksymalnego skojarzenia
        w grafach dwudzielnych.
    -> Dodajemy sztuczne źródło s i ujście t.
    -> Zakładamy, że każda krawędź ze zbioru A jest skierowana do zbioru B oraz, że
        jej przepustowość wynosi 1.
    -> Maksymalnym skojarzeniem jest maksymalny przepływ z s do t.
"""