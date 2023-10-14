def solution(cipher, code):
    decrypted = [] #해독된 암호 문자열을 저장할 리스트 초기화
    #문자열 cipher 에서 code의 배수 번째 글자들을 추출하여 리스트에 저장
    for i in range(code-1, len(cipher), code):
        decrypted.append(cipher[i])
    decrypted_text = ''.join(decrypted)
    return decrypted_text