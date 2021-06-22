def _lis(A):
    """
    Function obtains length of Longest Increasing Subsequence
    in a given list.

    Let A be an array, and f(i) = length of LIS ending on A[i].
    """
    n = len(A)
    if n == 0:
        return "list is empty"

    F = [1 for _ in range(n)]  # Initially every subsequence has len=1.
    P = [-1 for _ in range(n)]  # Parent/Predecessor of each number.

    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j

    return max(F), F, P


def main():
    # Tests for Longest Increasing Subsequence.
    A = [13, 7, 21, 42, 8, 2, 44, 53]
    print(_lis(A))
    B = []
    print(_lis(B))
    C = [13]
    print(_lis(C))


if __name__ == "__main__":
    main()