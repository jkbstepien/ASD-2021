"""
W pewnym laboratorium genetycznym powstał ciąg sekwencji DNA. Każda sekwencja
to pewien napis składający się z symboli G, A, T, C. Przed dalszymi badaniami
konieczne jest upewnić się, że wszystkie sekwencje DNA są parami różne. Proszę
opisać algorytm, który sprawdza czy tak faktycznie jest.

Algorytm:
    -> Tworzymy drzewo, którego korzeń ma 4 dzieci (G, A, T, C).
    -> W konstruktorze klasy, której używamy do tworzenia węzłów dodajemy
        dodatkowe pole end, nominalnie ustawione na False, które będzie nam
        wyznaczać koniec danej sekwencji.
    -> Konstruujemy drzewo wszystkich sekwencji i sprawdzamy czy się one nie
        powtarzają.
    -> Jeśli przy dodawaniu określonej sekwencji okaże się, że nie musimy
        wstawiać do drzewa nowego węzła oraz, że sekwencja kończy się na węźle
        z end=True to w takim wypadku otrzymaliśmy duplikat.
"""