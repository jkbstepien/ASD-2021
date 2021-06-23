# zadanie obowiązkowe
# W problemie sumy podzbioru mamy dany ciąg liczb A[0],...,A[n-1]
# oraz liczbę T. Należy stwierdzić czy istnieje podciąg sumujący się dokładnie do T.


def subset_sum(A, T):
    def find(current_sum, i):
        if current_sum == T:
            return A != []  # taking care of case when A=[], T=0
        if i == -1:
            return False
        return find(current_sum + A[i], i - 1) or find(current_sum, i - 1)

    return find(0, len(A) - 1)


test_1 = subset_sum([1, 3, 5, 6], 10)
test_2 = subset_sum([1, 0, 1], 10)
test_3 = subset_sum([], 1)
test_4 = subset_sum([], 0)
test_5 = subset_sum([-5, 4], -1)
print(f"1:\t{test_1}\n"
      f"2:\t{test_2}\n"
      f"3:\t{test_3}\n"
      f"4:\t{test_4}\n"
      f"5:\t{test_5}\n")
