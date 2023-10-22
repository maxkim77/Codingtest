import itertools

def solution(spell, dic):
    for p in itertools.permutations(spell):
        word = ''.join(p)
        if word in dic:
            return 1
    return 2