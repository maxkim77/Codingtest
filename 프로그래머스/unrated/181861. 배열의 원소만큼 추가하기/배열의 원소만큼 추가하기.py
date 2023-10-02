def solution(arr):
    X = [] #빈배열 X를 생성합니다.
    for a in arr: #배열 arr의 각원소에 대해서
        X.extend([a] * a) #원소a를 a번 배열X의 맨뒤에 추가합니다.
    return X #배열 X를 반환합니다.