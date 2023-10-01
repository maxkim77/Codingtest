def transform(arr):
    # 주어진 조건에 따라 arr의 각 원소를 변환합니다.
    for i in range(len(arr)):
        if arr[i] >= 50 and arr[i] % 2 == 0:
            arr[i] //= 2
        elif arr[i] < 50 and arr[i] % 2 == 1:
            arr[i] = arr[i] * 2 + 1
    return arr

def solution(arr):
    x = 0  # 반복 횟수를 저장할 변수
    while True:
        # arr의 복사본을 만들고 변환합니다.
        prev_arr = arr.copy()
        arr = transform(arr)
        # 변환 후의 배열이 이전 배열과 동일한지 확인합니다.
        if prev_arr == arr:
            return x  # 동일하면 반복 횟수를 반환합니다.
        x += 1  # 동일하지 않으면 반복 횟수를 증가시킵니다.

