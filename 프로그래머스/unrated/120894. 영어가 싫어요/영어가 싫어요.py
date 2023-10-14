def solution(numbers):
    # 영어 단어와 해당하는 정수를 매핑하는 사전 생성
    word_to_number = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }

    result = 0  # 결과를 저장할 변수 초기화
    current_word = ""  # 현재 읽고 있는 영어 단어 저장용 변수 초기화

    # 문자열을 순회하면서 영어 단어를 읽어서 정수로 변환
    for char in numbers:
        current_word += char  # 현재 단어에 글자 추가

        # 현재 단어가 영어 단어 사전에 있을 때
        if current_word in word_to_number:
            result = result * 10 + word_to_number[current_word]
            current_word = ""  # 현재 단어 초기화

    return result