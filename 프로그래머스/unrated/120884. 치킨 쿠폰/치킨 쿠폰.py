def solution(chicken):
    coupons = chicken
    answer = 0
    
    while coupons >= 10:
        service_chicken = coupons // 10
        answer += service_chicken
        coupons = coupons % 10
        coupons += service_chicken
        
    return answer