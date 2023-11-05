def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        sliced = sorted(array[i-1:j])
        answer.append(sliced[k-1])
    return answer