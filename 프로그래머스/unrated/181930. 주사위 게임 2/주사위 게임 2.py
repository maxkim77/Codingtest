def solution(a, b, c):
    
    if a != b and b != c and a != c:
        answer = a + b + c
    elif (a == b and b != c) or (a != b and b == c) or (a == c and b != c):
        answer = (a + b + c) * (a**2 + b**2 + c**2)
    elif a == b == c:
        answer = (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
        
    return answer