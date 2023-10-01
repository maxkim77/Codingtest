def solution(arr, k):
    if k % 2 == 1:
        #홀 수 인경우 k를 곱함
        result = [x * k for x in arr]
    else:
        #그밖에 k를 더함
        result = [x + k for x in arr]
    return result