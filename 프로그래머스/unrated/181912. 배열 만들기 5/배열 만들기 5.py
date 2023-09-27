def solution(intStrs, k, s, l):
    answer = []
    
    for intStr in intStrs:
        substring = intStr[s:s+l]
        integer_value = int(substring)
        
        if integer_value > k:
            answer.append(integer_value)
            
    return answer