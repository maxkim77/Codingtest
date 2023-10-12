def solution(n):
    factors = []
    #2부터 시작하여 n까지의 모든 숫자로 n을 나눈다.
    
    for i in range(2, n+1):
        #n이 i로 나누어 떨어진다면
        while n % i == 0:
            #i는 소인수입니다.
            if i not in factors:
                factors.append(i)
                #n을 i로 나눕니다.
            n /= i
            
        if n == 1:
            break            
                
    return factors