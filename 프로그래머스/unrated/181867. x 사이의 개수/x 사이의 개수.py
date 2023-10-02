def solution(myString):
    split_strings = myString.split('x')
    return [len(s) for s in split_strings]