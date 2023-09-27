def solution(my_strings, parts):
    result = ""
    
    for i in range(len(my_strings)):
        s, e = parts[i]
        substring = my_strings[i][s:e+1]
        result += substring
        
    answer = result
    return answer