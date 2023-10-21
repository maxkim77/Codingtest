def solution(array):
    count_of_7 = 0
    for num in array:
        count_of_7 += str(num).count('7')
    return count_of_7