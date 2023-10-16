def solution(num, k):
    str_num = str(num)  # 정수를 문자열로 변환
    for i, digit in enumerate(str_num):
        if int(digit) == k:
            return i + 1  # 처음으로 일치하는 숫자의 위치를 반환
    return -1  # 일치하는 숫자가 없으면 -1을 반환