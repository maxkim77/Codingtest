def solution(myString, pat):
    #pat의 마지막 인덱스를 찾습니다.
    last_index = myString.rfind(pat) + len(pat)
    return myString[:last_index]