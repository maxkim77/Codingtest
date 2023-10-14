def solution(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    unique_chars = []
    
    for char, count in char_count.items():
        if count == 1:
            unique_chars.append(char)
     
    sorted_unique_chars = sorted(unique_chars)
    result = ''.join(sorted_unique_chars)
    return result