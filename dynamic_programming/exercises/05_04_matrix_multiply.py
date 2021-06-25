"""
Dany jest ciąg macierzy A1, A2,...,An. Ktoś chce policzyć iloczyn
A1, A2,...,An. Macierze nie są koniecznie kwadratowe (ale oczywiście znamy
ich rozmiary). Zależnie w jakiej kolejności wykonujemy mnożenia, koszt obliczeniowy
może być różny - należy podać algorytm znajdujący koszt mnożenia przy optymalnym
doborze kolejności.

    A      X     X    X    X        i - kolumny
    AB     B     X    X    X        j - wiersze
    ABC    BC    C    X    X
    ABCD   BCD   CD   D    X
    ABCDE  BCDE  CDE  DE   E


    F(i, j) - minimalny koszt pomnożenia macierzy od Ai do Aj.

    i > j:
        F(i, j) = 0
    i <= j:
        F(i, j) = min( F(i + 1, j) * F(i, j - 1),
                       F(i + 2, j) * F(i, j - 2),...
                       F(j, j) * F(i, 0)
                      )

    Wynik: F[n - 1][0]
"""
