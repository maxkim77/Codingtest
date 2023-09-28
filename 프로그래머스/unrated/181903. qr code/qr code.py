def solution(q, r, code):
    # 결과를 저장할 빈 문자열을 생성합니다.
    result = ''
    
    # code의 각 인덱스에 대해,
    for i in range(len(code)):
        # 인덱스를 q로 나누었을 때의 나머지가 r인지 확인합니다.
        if i % q == r:
            # 나머지가 r이라면, 해당 인덱스의 문자를 result에 추가합니다.
            result += code[i]
    
    # result를 반환합니다.
    return result