def solution(numLog):
    result = []
    for i in range(1, len(numLog)):
        diff = numLog[i] - numLog[i-1]
        if diff == 1:
            result.append("w")
        elif diff == -1:
            result.append("s")
        elif diff == 10:
            result.append("d")
        elif diff == -10:
            result.append("a")
    answer = ''.join(result)
    return answer