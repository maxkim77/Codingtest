def solution(n):
    #n명의 사람들이 최소 한조각씩 먹기 위해 필요한 피자의 수계산
    return n // 7 + (1 if n % 7 != 0 else 0)