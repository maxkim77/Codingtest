def solution(before, after):
    # 두 문자열의 길이가 다르면, 'after'를 만들 수 없으므로 0을 반환합니다.
    if len(before) != len(after):
        return 0

    # 각 문자열에서 문자의 발생 횟수를 세기 위한 딕셔너리를 생성합니다.
    before_count = {}
    after_count = {}

    # 'before' 문자열의 각 문자를 세고, 딕셔너리에 저장합니다.
    for char in before:
        if char in before_count:
            before_count[char] += 1
        else:
            before_count[char] = 1

    # 'after' 문자열의 각 문자를 세고, 딕셔너리에 저장합니다.
    for char in after:
        if char in after_count:
            after_count[char] += 1
        else:
            after_count[char] = 1

    # 두 딕셔너리가 동일한지 확인합니다. 동일하다면 'before'에서 'after'를 만들 수 있으므로 1을 반환합니다.
    # 그렇지 않다면, 'after'를 만들 수 없으므로 0을 반환합니다.
    if before_count == after_count:
        return 1
    else:
        return 0
