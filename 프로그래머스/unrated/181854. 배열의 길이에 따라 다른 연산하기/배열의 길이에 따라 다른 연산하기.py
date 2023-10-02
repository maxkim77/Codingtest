def solution(arr, n):
    # 배열의 길이가 홀수인지 짝수인지 확인합니다.
    is_odd_length = len(arr) % 2 == 1

    # 결과를 저장할 빈 배열을 생성합니다.
    result = []

    # 주어진 배열을 순회합니다.
    for i, num in enumerate(arr):
        # 배열의 길이가 홀수이고 현재 인덱스가 짝수인 경우,
        # 또는 배열의 길이가 짝수이고 현재 인덱스가 홀수인 경우
        if (is_odd_length and i % 2 == 0) or (not is_odd_length and i % 2 == 1):
            # 현재 숫자에 n을 더하여 result에 추가합니다.
            result.append(num + n)
        else:
            # 그렇지 않은 경우 현재 숫자를 그대로 result에 추가합니다.
            result.append(num)

    # 결과 배열을 반환합니다.
    return result