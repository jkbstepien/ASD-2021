# Mamy daną tablicę z nominałami monet stosowanych w pewnym dziwnym kraju,
# oraz kwotę T. Proszę podać algorytm, który oblicza minimalną ilość monet
# potrzebną do wydania kwoty T (algorytm zachłanny, wydający najpierw
# największą monetę, nie działa: dla monet 1, 5, 8 wyda kwotę 15 jako
# 8 + 5 + 1 + 1 zamiast 5 + 5 + 5).


def coin_change(coins, T):
    INF = float('inf')  # as we later use function min() it's convenient to initialize array with extra large values.
    min_coins = [INF] * (T + 1)  # array will hold the min number of coins for each amount from 0 to T.

    min_coins[0] = 0  # there are 0 ways to make amount 0 with positive coin values.
    for coin in coins:
        for i in range(T + 1):
            if i - coin >= 0:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    if min_coins[T] != INF:
        return min_coins[T]
    else:
        return -1


test_coins = [1, 5, 8]
print(coin_change(test_coins, 15))
