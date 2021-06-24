"""
Dana jest szachownica A o wymiarach n x n. Szachownica zawiera liczby wymierne.
Należy przejść z pola (1, 1) na pole (n, n) korzystając jedynie z ruchów 'w dół'
oraz 'w prawo'. Wejście na dane pole kosztuje tyle, co znajdująca się tam liczba.
Proszę podać algorytm znajdujący trasę o minimalnym koszcie.
"""
from random import randint


def chessboard_tour(A):
    n = len(A)
    # dp array will contain min cost to reach each square.
    dp = [[float("inf") for _ in range(n)] for _ in range(n)]
    dp[0][0] = A[0][0]

    # Fill first row and first column because min cost
    # for them is just sum of elements in row/column.
    for i in range(1, n):
        dp[0][i] = dp[0][i - 1] + A[0][i]
        dp[i][0] = dp[i - 1][0] + A[i][0]

    # Each square can be reached only from left or top, so
    # min value of tile is min(left, top) + cost of chosen square.
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + A[i][j]

    print(*dp, sep='\n')
    return dp[n - 1][n - 1]


def main():
    # Tests for chessboard_tour.
    n = 4
    array = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            array[i][j] = randint(1, 10)

    print(*array, sep='\n')
    print()
    print(f"\nanswer: {chessboard_tour(array)}")


if __name__ == "__main__":
    main()
