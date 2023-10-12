def solution(my_string):
    #합계를 저장할 변수를 초기화
    total = 0
    
    #문자열 my_string을 순회하면서 각 문자를 확인합니다.
    for char in my_string:
        if char.isdigit():
            
            total += int(char)
    return total