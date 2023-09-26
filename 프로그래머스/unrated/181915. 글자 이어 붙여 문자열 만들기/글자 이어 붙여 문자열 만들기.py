def solution(my_string, index_list):
    # 리스트 컴프리헨션을 사용하여 index_list에 주어진 인덱스들에 해당하는 문자들을 순서대로 이어붙입니다.
    result_string = ''.join([my_string[i] for i in index_list])
    return result_string