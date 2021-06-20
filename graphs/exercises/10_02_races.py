"""
Król Bitocji postanowił zorganizowac serie wyscigów samochodowych. Wyscigi
maja sie odbywac po trasach zamknietych, składajacych sie z odcinków autostrady łaczacych miasta Bitocji.
Król chce, zeby kazde miasto było zaangazowane w dokładnie jeden wyscig. W tym celu nalezy sprawdzic,
czy da sie wynajac odpowiednie odcinki autostad. Nalezy jednak pamietac o nastepujacych ograniczeniach:
    1. w Bitocji wszystkie autostrady sa jednokierunkowe,
    2. z kazdego miasta wychodza co najwyzej dwa odcinki autostrady, którymi mozna dojechac do innych
        miast,
    3. do kazdego miasta dochodza co najwyzej dwa odcinki autostrady, którymi mozna przyjechac z innych
        miast,

Prosze zaproponowac algorytm, który majac na wejsciu opis sieci autostrad Bitocji sprawdza czy da sie
zorganizowac serie wyscigów tak, zeby przez kazde miasto przebiegała trasa dokładnie jednego.

Utrudnienie: Kazdy odcinek autostrady ma przedział dopuszczalnych cen i nalezy wybrac wspólna cene
dla wszystkich wynajetych odcinków.

Algorytm:
    Tak naprawdę w tym zadaniu chcemy pokryć cały nasz graf cyklami.
    Zakładamy, że te cykle są proste - żaden nie przechodzi przez jedno miasto dwa razy.
    Zmienne kojarzymy z nie z miastami, a z krawędziami.
    Do wyboru poszczególnych ścieżek korzystamy z XOR'ów
    np. (1 ^ 4) and 2 and (3 ^ 6) and (5 ^ 7) and (8 ^ 9) and (10 ^ 11).
    Bierzemy dowolną krawędź, która jest w wyrażeniu.
        Np. Sprawdzamy czy 4 występuje w naszych trasach, następnie sprawdzamy czy jest
        5 lub 7 i idziemy tak, aż wyznaczymy jedną trasę, a potem kolejną itd.
    Cykle, które otrzymamy na pewno są rozłączne bo przez każde miasto prowadzi tylko
    jedna ścieżka.
"""