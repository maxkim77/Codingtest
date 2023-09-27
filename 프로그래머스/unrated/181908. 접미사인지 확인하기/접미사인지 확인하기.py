def solution(my_string, is_suffix):
    answer = 0  # 초기값을 0으로 설정합니다.
    # my_string의 끝에서 is_suffix의 길이만큼의 부분 문자열을 추출합니다.
    suffix = my_string[-len(is_suffix):]
    # 추출된 부분 문자열이 is_suffix와 동일한지 확인하고, 동일한 경우 answer를 1로 설정합니다.
    if suffix == is_suffix:
        answer = 1
    return answer  # 결과를 반환합니다.
