def maximin(A, k):
    """
    Problem można rozważać na przykładzie robotników i fragmentów płotu, który
    mają pomalować.
    Wówczas nasza funkcja F będzie wyglądać:
        F(i, t) = maksymalna wartość podziału a_0, ...,a_i na t ciągów.
        t utożsamiamy z robotnikiem/ami malującymi fragment płotu.
    Niech x - indeks tablicy A:
        F(i, t) = min( F(i - x, t - 1), suma od j=x+1 do i: A[j] )
    """
    n = len(A)
    F = [[0 for _ in range(k + 1)] for _ in range(n)]

    # Calculate sums of coherent subsequences (i,...,j).
    prefix_sums = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        prefix_sums[i][i] = A[i]
        for j in range(i + 1, n):
            prefix_sums[i][j] = prefix_sums[i][j - 1] + A[j]

    # Initialize F's first column with pref-sums of A.
    # For one worker it is always sum of whole A array.
    F[0][1] = A[0]
    for i in range(1, n):
        F[i][1] = F[i - 1][1] + A[i]

    for i in range(n):
        for t in range(1, k + 1):
            for j in range(1, i + 1):
                F[i][t] = max(F[i][t], min(F[i - j][t - 1], prefix_sums[i - j + 1][i]))

    return F[n - 1][k], F


def main():
    array = [1, 2, 3, 4]

    k = 2
    result, F = maximin(array, k)
    print(*F, sep='\n')
    print(f"result = {result}\n")

    k = 3
    result, F = maximin(array, k)
    print(*F, sep='\n')
    print(f"result = {result}\n")


if __name__ == "__main__":
    main()
