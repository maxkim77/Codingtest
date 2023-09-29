def solution(n,k):
    answer = [] #결과를 저장할 빈 배열을 초기화합니다.
    for i in range(1, n + 1): #1부터 n까지의 정수에 대해 반복합니다.
        if i % k == 0: # i가 k의 배수인지 확인합니다.
            answer.append(i)# i가 k의 배수인 경우, 결과 배열에 i를 추가합니다.
    return answer