from collections import Counter
def solution(strArr):
    #문자열의 길이를 세어서 Counter 객체를 생성
    length_counts = Counter(len(s) for s in strArr)
    #가장 흔한 문자열 길이의 개수를 찾아 반환합니다.
    return length_counts.most_common(1)[0][1]