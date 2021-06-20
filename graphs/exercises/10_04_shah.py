"""
Algocja lezy na wielkiej pustyni i składa sie z miast oraz oaz połaczonych drogami.
Kazde miasto jest otoczone murem i ma tylko dwie bramy—północna i południowa. Z kazdej bramy prowadzi
dokładnie jedna droga do jednej oazy (ale do danej oazy moze dochodzic dowolnie wiele dróg; oazy moga tez
byc połaczone drogami miedzy soba). Prawo Algocji wymaga, ze jesli ktos wjechał do miasta jedna brama,
to musi go opuscic druga. Szach Algocji postanowił wysłac gonca, który w kazdym miescie kraju odczyta
zakaz formułowania zadan “o szachownicy” (obraza majestatu). Szach chce, zeby goniec odwiedził kazde
miasto dokładnie raz (ale nie ma ograniczen na to ile razy odwiedzi kazda z oaz). Goniec wyjezdza ze stolicji
Algocji, miasta x, i po odwiedzeniu wszystkich miast ma do niej wrócic.
Prosze przedstawic algorytm, który stwierdza czy odpowiednia trasa gonca istnieje.

Algorytm:
    Na naszym grafie rozróżniamy oazy i miasta.
    Oazy mogą być połączone bezpośrednio ze sobą.
    Łączymy wszystkie oazy, które mają ze sobą wspólną krawędź (można przejść z jednej do drugiej).
    Na naszym uproszczonym grafie z połączonymi już oazami (z jedną lub więcej - super-oazą),
    szukamy cyklu Eulera.
    Jeżeli istnieje to znaczy, że goniec może wyruszyć z miasta X, odwiedzić wszystkie pozostałe miasta
    i wrócić.

    Można nasz graf jeszcze bardziej uprościć:
        Jeżeli otrzymamy miasto, którego bramy - północna i południowa, prowadzą do tej samej oazy,
        to możemy usunąć ten wierzchołek-miasto i zostawić pętlę wskazującą na samą oazę.
        Po usunięciu niepotrzebnych wierzchołków nasz graf staje się jeszcze mniejszy.
"""