import math
def solution(balls, share):
    answer = 0
    mother = math.factorial(balls)
    son = math.factorial(balls - share) * math.factorial(share)
    answer = mother/son
    return answer