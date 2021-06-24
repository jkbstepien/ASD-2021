"""
Asystent znanego profesora otrzymał polecenie wyliczenia sumy pewnego ciągu liczb (liczby mogą
być zarówno dodatnie jak i ujemne):
n 1 + n 2 + ... + n k
Aby zminimalizować błędy zaokrągleń asystent postanowił wykonać powyższe dodawania w takiej
kolejności, by największy co do wartości bezwzględnej wynik tymczasowy (wynik każdej operacji
dodawania; wartość końcowej sumy również traktujemy jak wynik tymczasowy) był możliwie jak
najmniejszy. Aby ułatwić sobie zadanie, asystent nie zmienia kolejności liczb w sumie a jedynie
wybiera kolejność dodawań.

Napisz funkcję opt sum, która przyjmuje tablicę liczb n 1 , n 2 , . . . , n k (w kolejności w jakiej wystę-
pują w sumie; zakładamy, że tablica zwiera co najmniej dwie liczby) i zwraca największą wartość
bezwzględną wyniku tymczasowego w optymalnej kolejności dodawań. Na przykład dla tablicy
wejściowej:
[1, −5, 2]
funkcja powinna zwrócić wartość 3, co odpowiada dodaniu −5 i 2 a następnie dodaniu 1 do wyniku.
Uzasadnij poprawność zaproponowanego rozwiązania i oszacuj jego złożoność obliczeniową.
"""


def opt_sum(array):
    """
    F(i, j) - najmniejszy wynik tymczasowy od i do j.
    """
    n = len(array)
    F = [[float("inf") for _ in range(n)] for _ in range(n)]

    prefix_sums = [0 for _ in range(n)]
    prefix_sums[0] = array[0]
    for i in range(1, n):
        prefix_sums[i] = prefix_sums[i - 1] + array[i]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            for k in range(j - i):
                F[i][j] = min(F[i][j],
                              abs(prefix_sums[j] - prefix_sums[i]),
                              max(F[i + k + 1][j], F[i][i + k]))

    return F[0][n - 1]


def main():
    tab1 = [1, -5, 2]  # Should return 3.
    tab2 = [1, 2, 3, 4, -5]  # Should return 2.
    print(opt_sum(tab2))


if __name__ == "__main__":
    main()
