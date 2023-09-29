def solution(arr, intervals):
    # intervals에서 각 구간의 시작 인덱스와 끝 인덱스를 추출합니다.
    a1, b1 = intervals[0]
    a2, b2 = intervals[1]
    
    # arr에서 첫 번째 구간과 두 번째 구간을 슬라이싱하여 추출합니다.
    # 인덱스는 0부터 시작하므로 각 인덱스에 1을 빼줍니다.
    first_interval = arr[a1:b1+1]  # 수정: 인덱스에 1을 빼줍니다.
    second_interval = arr[a2:b2+1]  # 수정: 끝 인덱스에 1을 더해줍니다.
    
    # 두 구간을 연결하여 새로운 배열을 만들고 반환합니다.
    new_array = first_interval + second_interval
    return new_array

# 예제 입력 및 함수 호출
arr = [1, 2, 3, 4, 5]
intervals = [[1, 3], [0, 4]]
result = solution(arr, intervals)
print(result)  # 출력: [2, 3, 4, 1, 2, 3, 4, 5]
