def solution(arr):
    rows = len(arr) #행의수
    cols = len(arr[0]) #열의수

    # 행의 수와 열의 수가 같다면 arr을 그대로 반환
    if rows == cols:
        return arr
    
    # 행의 수가 더 많은 경우
    if rows > cols:
        for i in range(rows):
            arr[i] += [0] * (rows - cols)
        return arr

    # 열의 수가 더 많은 경우
    else:
        # 각 열의 끝에 0을 추가
        for i in range(cols -rows):
            arr.append([0] * cols)
        return arr