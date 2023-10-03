def jaccard_similarity(str1, str2):
    str1, str2 = str1.upper(), str2.upper()
    
    # Extract two-letter elements from the string and store it in a list
    def extract_elements(s):
        return [s[i:i+2] for i in range(len(s)-1) if s[i:i+2].isalpha()]
    
    elements1 = extract_elements(str1)
    elements2 = extract_elements(str2)
    
    # If both are empty, return 1
    if not elements1 and not elements2:
        return 1

    # Find the intersection of two lists
    intersection = sum((min(elements1.count(e), elements2.count(e)) for e in set(elements1)))
    
    # Find the union of two lists
    union = len(elements1) + len(elements2) - intersection
    
    return intersection / union


def solution(str1, str2):
    return int(jaccard_similarity(str1, str2) * 65536)
