def fib(n):
    """
    Recursive function for n-th number in fibonacci sequence.
    """
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def dp_fib(n):
    """
    DP approach to fib sequence.
    """
    F = [1 for _ in range(n + 1)]

    for i in range(3, n + 1):
        F[i] = F[i - 1] + F[i - 2]

    return F[n]


print(fib(7))
print(dp_fib(7))
