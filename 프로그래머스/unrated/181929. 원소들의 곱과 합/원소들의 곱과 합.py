def solution(num_list):
    product = 1
    for num in num_list:
        product *= num
        
    sum_of_elements = sum(num_list)
    answer = 1 if product < sum_of_elements ** 2 else 0
    return answer