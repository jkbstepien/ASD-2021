"""
Jakub Stępień

Złożoność obliczeniowa: O(nlogn).
Złożoność pamięciowa: O(n).

Zapamiętujemy na jakich indeksach początkowych były nasze liczby w tablicy.
Sortujemy tablicę krotek: (liczba, jej indeks) używając stabilnego sortowania przez scalanie,
a następnie obliczamy w pętli maksymalną różnicę w pozycjach korzystając z zapamiętanych wcześniej indeksów.
Algorytm sortowania jest stabilny, oznacza to, że żaden z elementów nie został przesunięty o więcej pól, niż musiał by
tablica została posortowana. Dlatego wynikiem jest nasz współczynnik nieuporządkowania.
"""
from zad1testy import runtests


def mergesort(T):
    if len(T) > 1:
        q = int(len(T) / 2)
        T_left = T[:q]
        T_right = T[q:]

        mergesort(T_left)
        mergesort(T_right)

        i = j = k = 0
        while i < len(T_left) and j < len(T_right):
            if T_left[i] < T_right[j]:
                T[k] = T_left[i]
                i += 1
            else:
                T[k] = T_right[j]
                j += 1
            k += 1

        while i < len(T_left):
            T[k] = T_left[i]
            i += 1
            k += 1
        while j < len(T_right):
            T[k] = T_right[j]
            j += 1
            k += 1
    return T


def chaos_index( T ):
    n = len(T)

    if len(T) == 1:
        return 0

    for i in range(n):
        T[i] = (T[i], i)
    mergesort(T)

    k = 0
    for i in range(n):
        k = max(k, T[i][1] - i, -T[i][1] + i)
    return k


runtests( chaos_index )
