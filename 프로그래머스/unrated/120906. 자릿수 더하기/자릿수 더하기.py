def solution(n):
    str_n = str(n)
    sum_digits = sum(int(digit) for digit in str_n)
    return sum_digits