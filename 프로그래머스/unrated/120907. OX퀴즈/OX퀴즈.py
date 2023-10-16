def solution(quiz):
    result = []  # 결과를 저장할 배열 초기화
    for equation in quiz:
        # 수식을 공백을 기준으로 분해하여 피연산자와 연산자를 추출
        parts = equation.split()
        X, operator, Y, equals_sign, Z = parts  # 변수에 각 부분 할당
        
        # 연산 수행
        if operator == '+':
            calc_result = int(X) + int(Y)
        else:
            calc_result = int(X) - int(Y)
        
        # 계산 결과와 주어진 결과를 비교
        if calc_result == int(Z):
            result.append('O')
        else:
            result.append('X')
    return result
