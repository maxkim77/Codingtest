def solution(num_list):
    for index, num in enumerate(num_list):
        if num < 0:
            return index
    return -1