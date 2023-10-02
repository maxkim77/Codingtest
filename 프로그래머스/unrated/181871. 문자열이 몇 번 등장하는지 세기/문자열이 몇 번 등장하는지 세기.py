def solution(myString, pat):
    #pat의 등장 횟수를 저장할 변수를 초기화합니다.
    count = 0
    #myString의 길이아 pat의 길이를 구합니다.
    len_myString, len_pat = len(myString), len(pat)
    #myString의 각 인덱스에 대해 반복합니다.
    for i in range(len_myString - len_pat + 1):
        if myString[i:i+len_pat] == pat:
            count += 1
    return count