def solution(num_list):
    operation_count = 0
    
    for num in num_list:
        while num > 1:
            if num % 2 == 0:
                num //= 2
            else:
                num = (num -1) // 2
            operation_count += 1
    return operation_count