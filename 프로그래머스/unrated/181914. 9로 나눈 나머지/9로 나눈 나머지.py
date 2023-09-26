def solution(number):
    # 문자열 number의 각 자리 숫자를 정수로 변환하고 합을 구합니다.
    digit_sum = sum(int(digit) for digit in number)
    # 합을 9로 나눈 나머지를 반환합니다.
    remainder = digit_sum % 9
    return remainder