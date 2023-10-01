def solution(myString):
    # 먼저 문자열의 모든 대문자를 소문자로 변환
    myString = myString.lower()
    # 그런 다음 'a' 문자만 'A'로 변환
    result = myString.replace('a', 'A')
    return result
