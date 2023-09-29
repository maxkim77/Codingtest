str = input().strip() #사용자로 부터 문자열을 입력 받아 양쪽 끝의 공백을 제거

if 1 <= len(str) <= 10: #문자열 길이 1 이상 10이하인 경우 반복
    for c in str: # 문자열 str의 각 문자에 대해 반복
        print(c) #현재 문자를 출력