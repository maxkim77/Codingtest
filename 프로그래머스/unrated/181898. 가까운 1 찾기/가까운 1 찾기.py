def solution(arr, idx):
    # idx부터 시작하여 배열을 검색하고 값이 1인 인덱스를 찾습니다.
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    # 값이 1인 인덱스를 찾지 못하면 -1을 반환합니다.
    return -1