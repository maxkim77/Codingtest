def solution(polynomial):
    terms = polynomial.split(' + ')  # 다항식을 항별로 분리
    x_coeff = 0  # 일차항의 계수 초기화
    constant = 0  # 상수항의 계수 초기화

    for term in terms:
        if 'x' in term:  # 일차항의 경우
            if term == 'x':  # 계수가 1인 경우
                x_coeff += 1
            else:  # 그 외의 경우
                x_coeff += int(term[:-1])  # 계수만 추출하여 더함
        else:  # 상수항의 경우
            constant += int(term)  # 상수항의 계수 더함

    # 결과 문자열 생성
    result = ''
    if x_coeff == 1:
        result += 'x'
    elif x_coeff != 0:
        result += f'{x_coeff}x'

    if constant != 0:
        if result:  # 일차항이 있는 경우
            result += f' + {constant}'
        else:  # 일차항이 없는 경우
            result += f'{constant}'

    return result

