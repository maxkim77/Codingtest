def solution(score):
    #평균점수 계산
    averages = [(sum(scores) / 2, index) for index, scores in enumerate(score)]
    #평균점수 정렬
    sorted_averages = sorted(averages, key = lambda x: (-x[0], x[1]))
    #등수 매기기
    ranks = [0] * len(score)
    prev_avg = -1
    rank = 0
    for i, (avg, index) in enumerate(sorted_averages):
        if avg != prev_avg:
            rank = i + 1
        ranks[index] = rank
        prev_avg = avg
    # 결과 반환
    return ranks