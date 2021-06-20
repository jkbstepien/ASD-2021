"""
Dana jest formuła logiczna w postaci 2CNF. To znaczy, ze formuła jest
koniunkcja klauzuli, gdzie kazda klauzula to alternatywa dwóch literałów, a kazdy literał to zmienna lub jej
negacja. Przykładem formuły w postaci 2CNF nad zmiennymi x,y,z jest:
(x or y) and (¬x or z) and (¬z or ¬y).
Prosze podac algorytm, który w czasie wielomianowym stwierdza, czy istnieje wartosciowanie spełniajace
formułę.

Algorytm:
    Alternatywę dwóch zmiennych możemy przedstawić jako dwie implikacje:
        (x or y) <=> (¬x => y) and (¬y => x)
    Całą formułę możemy przedstawić jako graf implikacji, w którym
        dla każdej klauzuli mamy dwie krawędzie.
    Trzeba rozważyć 3 przypadki:
        1) istnieje w G krawędź postaci x => ¬x
            dla x = 1, ¬x = 0 FAŁSZ
            dla x = 0, ¬x = 1 PRAWDA
        2) istnieje w G krawędź postaci ¬x => x
            analogicznie jak w 1)
        3) istnieją w G krawędzie:
            (*) x => ¬x
            (**) ¬x => x
            żeby wyrażenie było spełnialne:
                (*) x = 0, (**) x = 1 co oznacza, że nie można tego spełnić

    Jeżeli nie zachodzi 1), 2) i 3) to istnieje takie wartościowanie, dla którego formuła
    SAT-2CNF jest spełnialna.
    Z punktu widzenia implementacji - jeżeli x i ¬x leżą w tej samej SSC to CNF jest niespełnialne.
"""