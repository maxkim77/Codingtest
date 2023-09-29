def solution(my_string, indices):
    char_list = list(my_string)
    
    for index in sorted(indices, reverse=True):
        del char_list[index]
    return ''.join(char_list)