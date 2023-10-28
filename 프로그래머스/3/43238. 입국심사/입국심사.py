def solution(n, times):
    minTime = 1
    maxTime = max(times) * n  # 가장 긴 심사 시간에 모든 인원이 심사받는 경우

    answer = maxTime
    while minTime <= maxTime:
        midTime = (minTime + maxTime) // 2
        total = sum(midTime // time for time in times)

        if total >= n:  # 주어진 시간에 모든 사람을 심사할 수 있는 경우
            answer = midTime
            maxTime = midTime - 1
        else:
            minTime = midTime + 1

    return answer