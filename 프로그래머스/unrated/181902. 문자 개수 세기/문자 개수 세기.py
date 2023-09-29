def solution(my_string):
    count_array = [0] * 52
    
    for char in my_string:
        if 'A' <= char <= 'Z':
            count_array[ord(char) - ord('A')] += 1
        elif 'a' <= char <= 'z':
            count_array[ord(char) - ord('a') + 26] += 1
    return count_array