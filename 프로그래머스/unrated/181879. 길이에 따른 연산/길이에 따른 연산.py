def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        product = 1
        for num in num_list:
            product *= num
        return product