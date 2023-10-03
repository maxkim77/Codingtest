from itertools import combinations

def solution(relation):
    num_rows = len(relation)
    num_cols = len(relation[0])
    
    # 가능한 모든 조합을 생성
    candidates = []
    for length in range(1, num_cols + 1):
        candidates.extend(combinations(range(num_cols), length))
    
    # 유일성을 확인
    unique_keys = []
    for candidate in candidates:
        tmp = [tuple([item[i] for i in candidate]) for item in relation]
        if len(set(tmp)) == num_rows:
            unique_keys.append(candidate)
    
    # 최소성을 확인
    answer = set(unique_keys)
    for i in range(len(unique_keys)):
        for j in range(i+1, len(unique_keys)):
            # 만약 한 조합이 다른 조합의 부분집합이라면 최소성을 만족하지 않음
            if set(unique_keys[i]) == set(unique_keys[i]) & set(unique_keys[j]):
                answer.discard(unique_keys[j])
                
    return len(answer)


