def solution(a, d, included):
    answer = 0  # 합을 저장할 변수 초기화
    for i, is_included in enumerate(included):
        if is_included:  # included 배열에서 true인 항만 더함
            answer += a + i * d  # 등차수열의 일반항을 사용하여 항의 값을 계산하고 더함
    return answer  # 합을 반환
