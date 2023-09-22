def solution(num_list):
    answer = 0
    odd_str = ''
    even_str = ''
    
    for num in num_list:
        if num % 2 == 0:
            even_str += str(num)
        else:
            odd_str += str(num)
    answer = int(odd_str) + int(even_str)
    
    
    return answer