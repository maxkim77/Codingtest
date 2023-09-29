def solution(arr):
    first_index = None
    last_index = None
    for index, value in enumerate(arr):
        if value == 2:
            if first_index is None:
                first_index = index
            last_index = index
    if first_index is None:
        return[-1]
    return arr[first_index:last_index+1]