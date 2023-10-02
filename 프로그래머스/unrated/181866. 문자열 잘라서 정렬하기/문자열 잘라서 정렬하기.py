def solution(myString):
    # 'x'를 기준으로 문자열을 나눕니다.
    split_strings = myString.split('x')
    split_strings = [s for s in split_strings if s]
    return sorted(split_strings)