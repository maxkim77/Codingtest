def solution(my_string, m, c):
    # 문자열의 길이를 m으로 나누어 몇 줄이 필요한지 계산합니다.
    num_lines = len(my_string) // m
    
    # 결과를 저장할 빈 문자열을 생성합니다.
    result = ''
    
    # 각 줄에 대해 c번째 문자를 result에 추가합니다.
    for i in range(num_lines):
        # c번째 문자의 인덱스를 계산합니다.
        index = (i * m) + (c - 1)
        # c번째 문자를 result에 추가합니다.
        result += my_string[index]
    
    return result