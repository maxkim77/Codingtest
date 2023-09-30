def solution(num_list):
    odd_number = 0
    even_number = 0
    for index, num in enumerate(num_list):
        if index % 2 == 1:
            odd_number += num
        else:
            even_number += num
    return max(odd_number, even_number)