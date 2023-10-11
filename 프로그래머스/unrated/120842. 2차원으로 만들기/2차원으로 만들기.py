def solution(num_list, n):
    result = []
    
    for i in range(0, len(num_list), n):
        result.append(num_list[i:i+n])
    return result