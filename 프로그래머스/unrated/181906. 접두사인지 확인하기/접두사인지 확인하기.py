def solution(my_string, is_prefix):
    # my_string의 앞부분이 is_prefix와 동일한지 확인하고 결과를 반환합니다.
    return 1 if my_string.startswith(is_prefix) else 0
