def solution(rsp):
    win_dict = {
        '2': '0',
        '0': '5',
        '5': '2'
    }
    
    answer = ''.join([win_dict[char] for char in rsp])
    
    return answer