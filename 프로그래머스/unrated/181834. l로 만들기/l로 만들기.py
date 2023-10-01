def solution(myString):
    result = ''
    for char in myString:
        if char < 'l':
            result += 'l'
        else:
            result += char
    return result