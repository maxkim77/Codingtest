def solution(letter):
    morse_list = [
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
        "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
        "..-", "...-", ".--", "-..-", "-.--", "--.."
    ]
    
    alphabet_list = 'abcdefghijklmnopqrstuvwxyz'
    
    morse_dict = {morse: alphabet for morse, alphabet in zip(morse_list, alphabet_list)}
    morse_split = letter.split(' ')
    decoded = ''.join([morse_dict[morse] for morse in morse_split])
    
    return decoded
