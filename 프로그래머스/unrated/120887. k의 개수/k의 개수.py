def solution(i, j, k):
    count = 0
    for num in range(i, j + 1):
        count += str(num).count(str(k))
    return count