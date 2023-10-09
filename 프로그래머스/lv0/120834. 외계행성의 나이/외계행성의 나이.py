def solution(age):
    digits = list(map(int, str(age)))
    
    letters = [chr(97 + digit) for digit in digits]
    return ''.join(letters)