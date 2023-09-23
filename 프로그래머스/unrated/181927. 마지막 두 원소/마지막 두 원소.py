def solution(num_list):

    last = num_list[-1]
    second = num_list[-2]
    
    if last > second:
        num_list.append(last-second)
    else:
        num_list.append(last * 2)

    answer = num_list
    return answer