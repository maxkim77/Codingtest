def solution(my_string, s, e):
    # 문자열을 세 부분으로 나눕니다.
    part1 = my_string[:s]
    part2 = my_string[s:e+1]
    part3 = my_string[e+1:]
    
    # 두 번째 부분을 뒤집습니다.
    reversed_part2 = part2[::-1]
    
    # 세 부분을 다시 합쳐서 결과 문자열을 만듭니다.
    result = part1 + reversed_part2 + part3
    
    return result
