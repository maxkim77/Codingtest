def solution(strArr):
    result = []
    
    for i, s in enumerate(strArr):
        if i % 2 == 0:
            result.append(s.lower())
        else:
            result.append(s.upper())
    
    return result