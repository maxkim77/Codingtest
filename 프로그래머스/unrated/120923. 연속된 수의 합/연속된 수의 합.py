def solution(num, total):
    mid = total // num
    if num % 2 == 0:
        start = mid - (num // 2) + 1
    else: 
        start = mid - (num//2)
    
    return [start + i for i in range(num)]