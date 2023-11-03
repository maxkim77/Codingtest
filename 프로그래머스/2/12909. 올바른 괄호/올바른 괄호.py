def solution(s):
    counter = 0
    for bracket in s:
        if bracket == '(':
            counter += 1
        else:
            counter -= 1
            
        #언제든지 닫는 괄호가 더 많아지면 올바르지 않은 괄호임
        if counter < 0:
            return False
        
    return counter == 0

    answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return True