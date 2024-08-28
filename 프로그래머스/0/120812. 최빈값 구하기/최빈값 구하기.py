from collections import Counter

def solution(array):
    #배열의 각 원소의 빈도수 계산
    freq = Counter(array)
    
    #가장 높은 빈도수 찾기
    max_freq = max(freq.values())
    
    #가장 높은 빈도수를 가진 원소들 찾기
    mode_values = [key for key, value in freq.items() if value == max_freq]
    
    #최빈값이 1개만 있으면 그값을 반환, 그렇지 않으면 -1 반환
    if len(mode_values) == 1:
        return mode_values[0]
    else:
        return -1 