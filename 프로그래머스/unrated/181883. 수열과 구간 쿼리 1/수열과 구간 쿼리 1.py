def solution(arr, queries):
    for query in queries:
        start, end = query
        for i in range(start, end + 1):
            arr[i] += 1
        
    return arr