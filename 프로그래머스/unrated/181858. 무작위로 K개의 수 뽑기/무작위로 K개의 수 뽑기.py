def solution(arr, k):
    result = [] #결과를 저장할 빈 배열을 생성합니다.
    for num in arr: #arr배열을 순회
        if num not in result: #현재 숫자가 result에 없으면
            result.append(num) #result에 현재 숫자를 추가합니다.
        if len(result) == k: #result의 길이가 k에 도달하면 루프를 종료
            break
    return result + [-1] * (k - len(result))
#result의 길이가 k보다 작으면 나머지값을 -1로 채워 반환합니다.