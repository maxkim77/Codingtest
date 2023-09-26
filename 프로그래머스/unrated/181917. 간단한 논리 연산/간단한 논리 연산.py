def solution(x1, x2, x3, x4):
    # 논리합(OR) 연산을 수행합니다.
    or_result1 = x1 or x2
    or_result2 = x3 or x4
    
    # 논리곱(AND) 연산을 수행합니다.
    and_result = or_result1 and or_result2
    
    # 최종 결과를 반환합니다.
    return and_result
