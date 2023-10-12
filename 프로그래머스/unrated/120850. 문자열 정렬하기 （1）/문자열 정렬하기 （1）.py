def solution(my_string):
    # 숫자만을 저장할 리스트를 초기화합니다.
    numbers = []
    
    # 문자열 my_string을 순회하면서 각 문자를 확인합니다.
    for char in my_string:
        # 만약 문자가 숫자라면
        if char.isdigit():
            # 정수형으로 변환하여 numbers 리스트에 추가합니다.
            numbers.append(int(char))
    
    # numbers 리스트를 오름차순으로 정렬하고 반환합니다.
    return sorted(numbers)
