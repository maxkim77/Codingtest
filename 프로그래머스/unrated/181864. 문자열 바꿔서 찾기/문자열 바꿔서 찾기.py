def solution(myString, pat):
    swapped_string = myString.replace('A','X').replace('B','A').replace('X','B')
    return 1 if pat in swapped_string else 0