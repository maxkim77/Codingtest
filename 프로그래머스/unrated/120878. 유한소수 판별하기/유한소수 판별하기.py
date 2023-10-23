def solution(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    g = gcd(a, b)
    a, b = a// g, b // g
    
    while b % 2 == 0:
        b = b // 2
    while b % 5 == 0:
        b = b // 5
        
    if b == 1:
        return 1
    else:
        return 2