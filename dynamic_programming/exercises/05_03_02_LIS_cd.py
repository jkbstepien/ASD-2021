"""
1) Jak wykorzystać algorytm dla problemu najdłuższego wspólnego podciągu
do rozwiązania zadania najdłuższego rosnącego podciągu?
2) Na wykładzie podaliśmy algorytm działający w czasie O(n^2). Proszę podać
algorytm działający w czasie O(nlogn).
"""


def bs_search_iter(arr, left, right, value):
    while left <= right:
        mid = left + (right - 1) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def _lis(A):
    n = len(A)
    if n < 1:
        return None
    if n == 1:
        return A[0]

    B = [0 for _ in range(n)]
    B[0] = A[0]
    length = 1  # Length of LIS.

    for i in range(1, n):
        if A[i] < B[i]:
            B[0] = A[i]
        elif A[i] > B[length - 1]:
            B[length] = A[i]
            length += 1
        else:
            idx = bs_search_iter(B, 0, n - 1, A[i])
            B[idx] = A[i]

    print(B)
    return length


def main():
    A = [4, 0, 2, 10, 9, 12]
    print(_lis(A))  # Should return 3.


if __name__ == "__main__":
    main()
