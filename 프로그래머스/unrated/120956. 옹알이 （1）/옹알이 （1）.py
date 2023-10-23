from itertools import permutations
def solution(babbling):
    answer = 0
    pronounce = ["aya", "ye", "woo", "ma"]
    for i in range(1, len(pronounce)+1):
        for word in babbling:
            if word in map(lambda x: ''.join(x), permutations(pronounce, i)):
                answer += 1
    return answer   