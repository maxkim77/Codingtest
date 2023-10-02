def solution(str_list, ex):
    result = ''
    
    for string in str_list:
        if ex not in string:
            result += string
            
    return result