import math
def solution(arr):
    answer = []
    n = len(arr)
    next_pow_of_2 = 2 ** math.ceil(math.log(n,2))
    zeros_needed = next_pow_of_2 - n
    return arr + [0] * zeros_needed