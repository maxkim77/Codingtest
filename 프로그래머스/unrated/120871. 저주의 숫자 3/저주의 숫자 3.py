def solution(n):
    number = 0 #변환할 10진수 숫자
    count = 0 #3x 마을의 숫자 개수
    while count < n:
        number += 1
        # 숫자에 3이 포함되어 있거나, 숫자가 3의 배수인 경우 건너뜁니다.
        if '3' in str(number) or number % 3 == 0:
            continue
        count += 1 #숫자가 3x 마을의 규칙을 만족하면, 3x 마을 의숫자갯수를 1씩 증가합니다.
    return number # n번째 3x 마을의 숫자를 반환