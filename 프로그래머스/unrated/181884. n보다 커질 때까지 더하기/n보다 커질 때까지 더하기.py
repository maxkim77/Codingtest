def solution(numbers, n):
    sum_value = 0
    for number in numbers:
        sum_value += number
        if sum_value > n:
            return sum_value
    return sum_value
