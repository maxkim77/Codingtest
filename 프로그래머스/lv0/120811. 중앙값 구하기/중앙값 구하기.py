def solution(array):
    sorted_array = sorted(array)
    middle_index = len(sorted_array) // 2
    return sorted_array[middle_index]