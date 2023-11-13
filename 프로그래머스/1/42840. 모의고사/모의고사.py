def solution(answers):
    # 각 수포자의 답안 패턴 정의
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    # 각 수포자의 정답 수를 저장할 리스트
    scores = [0, 0, 0]
    
    # 정답과 비교하여 점수 계산
    for i in range(len(answers)):
        for j in range(3):
            if answers[i] == patterns[j][i % len(patterns[j])]:
                scores[j] += 1
    
    # 가장 많은 문제를 맞힌 사람 찾기
    max_score = max(scores)
    result = [i + 1 for i, score in enumerate(scores) if score == max_score]
    
    return result
