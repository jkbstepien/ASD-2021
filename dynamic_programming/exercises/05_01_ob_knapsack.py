def knapsack(W, P, max_w):
    n = len(W)
    F = [[0] * (max_w + 1) for i in range(n)]

    for w in range(W[0], max_w + 1):
        F[0][w] = P[0]
    for i in range(1, n):
        for w in range(1, max_w + 1):
            F[i][w] = F[i-1][w]
            if w >= W[i]:
                F[i][w] = max(F[i][w], F[i-1][w-W[i]] + P[i])

    return F[n-1][max_w], F


def get_solution(F, W, P, i, w):
    if i == 0:
        if w >= W[0]:
            return [0]
        else:
            return []
    if w >= W[i] and F[i][w] == F[i-1][w-W[i]] + P[i]:
        return get_solution(F, W, P, i - 1, w - W[i]) + [i]
    return get_solution(F, W, P, i - 1, w)


test_w = [4, 1, 2, 4, 3, 5, 10, 3]
test_w_1 = [10, 1, 2]
test_p = [7, 3, 2, 10, 4, 1, 7, 2]
test_p_1 = [20, 10, 11]
test_max_w = 12

x, y = knapsack(test_w_1, test_p_1, test_max_w)
print(x, y)
