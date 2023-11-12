from collections import deque

def is_one_diff(word1, word2):
    diff_count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff_count += 1
        if diff_count > 1:
            return False
    return diff_count == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = set()
    queue = deque([(begin, 0)])
    
    while queue:
        current_word, step = queue.popleft()
        visited.add(current_word)
        
        if current_word == target:
            return step
        
        for word in words:
            if word not in visited and is_one_diff(current_word, word):
                queue.append((word, step+1))
                
    return 0