def solution(my_string, num1, num2):
    # 문자열을 리스트로 변환하여 수정 가능한 형태로 변환
    string_list = list(my_string)

    # num1과 num2에 해당하는 인덱스의 문자 교환
    string_list[num1], string_list[num2] = string_list[num2], string_list[num1]

    # 리스트를 다시 문자열로 변환하여 결과 반환
    result = ''.join(string_list)
    
    return result