def discrete_knapsack(weights, profits, max_weight):
    n = len(weights)
    array = [[0] * (max_weight + 1) for _ in range(n)]

    # Fill first row with initial profits.
    for w in range(weights[0], max_weight + 1):
        array[0][w] = profits[0]

    for i in range(1, n):
        for w in range(1, max_weight + 1):
            array[i][w] = array[i - 1][w]
            # Determine whether it's worth to pick this item basing on profit.
            if w >= weights[i]:
                array[i][w] = max(array[i][w],
                                  array[i - 1][w - weights[i]] + profits[i])

    return array[n - 1][max_weight], array


def get_solution(results, weights, profits, i, w):
    if i == 0:
        if w >= weights[0]:
            return [0]
        else:
            return []
    if w >= weights[i]:
        if results[i][w] == results[i - 1][w - weights[i]] + profits[i]:
            return get_solution(results, weights, profits, i - 1, w - weights[i]) + [i]
        return get_solution(results, weights, profits, i - 1, w)


def main():
    # Tests for knapsack.
    weights = [10, 1, 2]
    profits = [20, 10, 11]
    max_w = 12
    result, array = discrete_knapsack(weights, profits, max_w)
    print(f"Profit: {result}")
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j], end='\t')
        print()

    tab = get_solution(array, weights, profits, len(weights) - 1, max_w)
    for elem in tab:
        print(f"picked item - {elem}")


if __name__ == "__main__":
    main()
