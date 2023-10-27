def solution(clothes):
    #각 의상 종류별로 의상수를 저장하는 딕셔너리를 초기화합니다.
    clothes_dict = {}
    #주어진 의상 목록을 순회 하며 각 의상 종류별로 의상수를 계산
    for name, category in clothes:
        clothes_dict[category] = clothes_dict.get(category,0) + 1
    #가능한 의상 조합수를 계산
    # 초기값을 1로 설정, 각 의상종류별 착용할 수 있는 옵션을 곱함
    
    combinations = 1
    for count in clothes_dict.values():
        combinations *= (count + 1) #착용하거나 착용하지 않는 옵션을 고려합니다.
    return combinations -1    
    answer = 0
    return ans