def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(n):
    return lcm(n, 6) // 6
