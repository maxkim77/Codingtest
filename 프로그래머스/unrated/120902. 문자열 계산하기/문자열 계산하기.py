def solution(my_string):
    #문자열을 공백을 기준으로 분리합니다.
    
    tokens = my_string.split()
    
    result = int(tokens[0])
    
    
    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        number = int(tokens[i + 1])
        #연산자에 따라 연산을 수행합니다.
        if operator == "+":
            result += number
        elif operator == '-':
            result -= number
    return result