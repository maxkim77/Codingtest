def solution(my_string):
    lower_string = my_string.lower()
    sorted_string = sorted(lower_string)
    answer = ''.join(sorted_string)
    return answer