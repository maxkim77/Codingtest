def solution(array):
    #max 함수를 사용하여 배열에서 가장 큰수를 찾습니다.
    max_value = max(array)
    #index 메서드를 사용하여 가장 큰수의 인덱스를 찾습니다.
    max_index = array.index(max_value)
    #가장 큰수와 그 수의 인덱스를 담은 배열을 반환합니다.
    answer = [max_value, max_index]
    return answer