def solution(numbers):
    #모든 숫자를 문자열로 변환
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    answer = ''.join(numbers)
    return str(int(answer))