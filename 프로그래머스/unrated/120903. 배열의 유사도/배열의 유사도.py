def solution(s1, s2):
    set1, set2 = set(s1), set(s2)
    intersection = set1.intersection(set2)
    return len(intersection)