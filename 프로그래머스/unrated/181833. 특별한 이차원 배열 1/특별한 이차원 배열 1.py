def solution(n):
    answer = [[]]
    arr = [[0 for _ in range(n)] for _ in range(n)] 
    for i in range(n):
        arr[i][i] = 1
    return arr