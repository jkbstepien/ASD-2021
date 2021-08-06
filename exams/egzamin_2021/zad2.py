"""
Jakub Stępień

Złożoność czasowa:O(n*m*log(n*m))
(czyli O(VlogV) dla V = n * m,
bo jest to graf rzadki - co najwyżej 3 krawędzie z jednego wierzchołka - lewo, prawo, przód)
Złożoność pamięciowa:O(n*m)
(Tablica trójwymiarowa o n*m*12 elementach + kolejka priorytetowa)
Opis:
Rozszerzam algorytm dijkstry. Każde wolne pole to grupa 12 wierzchołków odpowiadających 12 stanom
(każda z możliwych orientacji - 4, razy każda z możliwych prędkości - 3)
Każde przejście między krawędziami to jeden ruch (obrót, lub przejście do przodu). Możliwe ruchy w danym momencie
wyznacza funkcja possible_moves(graf, pozycja A, stan (zwrot i prędkość)).
Do kolejki dodaję te ruchy(a tak na prawdę wierzchołki, które osiągnę z odpowiednim kosztem),
które pozwalają mi na relaksacje danego wierzchołka docelowego (czyli kosztu dotarcia dla pozycji w tablicy + stanu).

Zaczynam od pozycji początkowej A i stanu 0 - zwrot w prawo, brak prędkości.

Dijkstra zwraca odległości od stanu początkowego dla każdego wierzchołka, zatem dla danej pozycji w tabeli jej odległość
od pozycji i stanu początkowego jest równa minimum z wierzchołków odpowiadających tej pozycji.

Zwracam zatem minimum z wartości na pozycji B.

Przyjąłem przeciwną reprezentację wiersz/kolumna, zatem na początku odwracam otzymany A i B.
"""
from zad2testy import runtests
from queue import PriorityQueue

right=0
down=1
left=2
up=3
speed_zero=0
speed_one=4
speed_two=8

def valid(graph, position):
    if position[0] >= len(graph) or position[0] < 0:
        return False
    if position[1] >= len(graph[0]) or position[1] < 0:
        return False
    if graph[position[0]][position[1]] == 'X':
        return False
    return True

def posible_moves(graph, A, state):
    direction = state % 4
    speed = int(state/4)
    moves = []
    moves += [(45, A, (direction + 1) % 4)]
    moves += [(45, A, (direction - 1) % 4)]
    move_cost = 60
    if speed == 1:
        move_cost = 40
    if speed == 2:
        move_cost = 30
    new_position = A
    if direction == right:
        new_position = (A[0], A[1] + 1)
    elif direction == left:
        new_position = (A[0], A[1] - 1)
    elif direction == up:
        new_position = (A[0] - 1, A[1])
    elif direction == down:
        new_position = (A[0] + 1, A[1])
    if valid(graph, new_position):
        moves += [(move_cost, new_position, direction + min(speed_two, 4*speed+4))]
    return sorted(moves)


def dijkstra(graph, A):
    n = len(graph)
    m = len(graph[0])
    queue = PriorityQueue()
    dist = [[[float('inf') for _ in range(12)] for _ in range(m)] for _ in range(n)]
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 'X':
                for k in range(12):
                    dist[i][j][k] = -1
    dist[A[0]][A[1]][0] = 0
    queue.put((0, 0, A))

    while not queue.empty():
        cost, state, position = queue.get()
        if dist[position[0]][position[1]][state] < cost:
            continue
        moves = posible_moves(graph, position, state)
        for move in moves:
            move_cost, new_position, new_state = move
            final_cost = cost+move_cost
            if dist[new_position[0]][new_position[1]][new_state] > final_cost:
                dist[new_position[0]][new_position[1]][new_state] = final_cost
                queue.put((final_cost, new_state, new_position))

    return dist


def robot(L, A, B):
    A = (A[1], A[0])
    B = (B[1], B[0])
    results = dijkstra(L, A)
    result = min(results[B[0]][B[1]])
    if result == float('inf'):
        return None
    return result


runtests(robot)
