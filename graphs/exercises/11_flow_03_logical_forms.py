"""
Dana jest formuła logiczna postaci: C_1 ∧ C_2 ∧ ... ∧ C_m, gdzie każda C_i to
klauzula będąca alternatywą zmiennych i/lub ich zaprzeczeń. Wiadomo, że
każda zmienna występuje w formule dokładnie dwa razy, raz zanegowana i raz
niezanegowana. Proszę podać algorytm, który oblicza takie wartości zmiennych, że
formuła jest prawdziwa.

Algorytm:
    -> Budujemy graf dwudzielny gdzie A to zbiór niezanegowanych zmiennych występujących
        w formule, zaś B to zbiór formuł C_1 ∧ C_2 ∧ ...
    -> Łączymy krawędzią każdą zmienną z formułą w której występuje (zanegowana / niezanegowana).
    -> Otrzymujemy graf, którego wierzchołki przy zmiennych mają stopień 2, bo każda zmienna
        występuje dokładnie dwa razy.
    -> Szukamy maksymalnego skojarzenia w grafie dwudzielnym.
    -> Jeśli maksymalne skojarzenie jest równe ilości zmiennych, to znaczy, że istnieje takie
        wartościowanie, dla którego formuła jest spełniona.
    -> Żeby określić wartościowanie zmiennych wystarczy sprawdzić czy formuła do której prowadzi
        zmienna ma zanegowaną wartość czy nie (odpowiednio 0/1).
    -> Jako, że w skojarzeniu może być maksymalnie jedna krawędź wychodząca z danej zmiennej,
        to nie jest możliwy przypadek, że którejś zmiennej przypiszemy zarówno 0 jak i 1.
        Zatem nasze rozumowanie jest poprawne.
"""