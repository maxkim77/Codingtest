def solution(a, d, included):
    answer = 0
    for i, is_included in enumerate(included):
        if is_included:
            answer += a + i * d
    return answer