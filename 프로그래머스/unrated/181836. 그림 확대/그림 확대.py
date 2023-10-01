def solution(picture, k): 
    result = []
    for row in picture:
        expanded_row = ''.join([char * k for char in row])
        for _ in range(k):
            result.append(expanded_row)
    return result