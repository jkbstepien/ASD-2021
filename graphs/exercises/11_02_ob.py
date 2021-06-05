"""
PL
Zaproponuj w jaki sposób można znaleźć maksymalny przepływ w sieci,
w której możliwe jest kilka źródeł i kilka ujść.

Algorytm:
    -> Stworzyć sztuczne źródło i ujście.
    -> Połączyć sztuczne źródło ze wszystkimi oryginalnymi źródłami.
    -> Połączyć wszystkie oryginalne ujścia ze sztucznym ujściem.
    -> Każdemu połączeniu ze sztucznego źródła do oryginalnego źródła
        przydzielić pojemność równą sumie pojemności wychodzących z
        oryginalnego źródła.
    -> Każdemu połączeniu z oryginalnego ujścia do sztucznego ujścia
        przydzielić pojemność równą sumie pojemności wchodzących do
        oryginalnego ujścia.
    -> Problem został sprowadzony do jednego źródła/ujścia. Możemy
        zastosować wybrany algorytm single-source/single-sink.

ENG
Propose algorithm to find max-flow while in network it is possible
to have multiple sources/sinks.

Algorithm:
    -> Create dummny source and sink.
    -> Connect dummy source with each original source.
    -> Connect all original sinks with our dummy sink.
    -> Each outgoing link from the dummy source to an original source
        gets assigned a capacity that is equal to the total capacity of
        the outgoing links from original source.
    -> Each incoming link from an original sink to the dummy sink gets
        assigned a capacity that is equal to the total capacity of the
        incoming links to original sink.
    -> Now we can use single-source/single-sink algorithm to find max-flow.
"""
