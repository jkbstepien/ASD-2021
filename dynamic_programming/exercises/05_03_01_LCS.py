"""
Mamy dwie tablice, A[n] i B[n]. Należy znaleźć długość ich
najdłuższego wspólnego podciągu. (Klasyczny algorytm dynamiczny O(n^2)).

_lcs_cohesionless - założenie, że podciąg nie musi być spójny.
"""


def _lcs_cohesionless(A, B):
    n = len(A)  # A and B are the same size.
    F = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if A[j - 1] == B[i - 1]:
                F[i][j] = F[i - 1][j - 1] + 1
            else:
                F[i][j] = max(F[i][j - 1], F[i - 1][j])

    print(*F, sep='\n')
    return F[n][n]


def main():
    A = [1, 2, 3, 7, 8, 9]
    B = [1, 2, 3, 9, 6, 7]
    print(f"{_lcs_cohesionless(A, B)}\n")  # Should return 4.


if __name__ == "__main__":
    main()

