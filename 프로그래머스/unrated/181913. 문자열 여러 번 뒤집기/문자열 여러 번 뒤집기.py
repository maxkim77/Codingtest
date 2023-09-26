def solution(my_string, queries):
    for query in queries:
        s, e = query  # 시작 인덱스와 끝 인덱스를 얻습니다.
        # 문자열의 s부터 e까지의 부분을 뒤집고, 나머지 부분과 합칩니다.
        my_string = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
    return my_string