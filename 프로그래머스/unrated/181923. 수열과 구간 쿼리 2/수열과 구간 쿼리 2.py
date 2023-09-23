def solution(arr, queries):
    answer = []
    
    for query in queries:
        s, e, k = query
        valid_values = [value for value in arr[s:e+1] if value > k]
        
        if valid_values:
            answer.append(min(valid_values))
        else:
            answer.append(-1)
    return answer