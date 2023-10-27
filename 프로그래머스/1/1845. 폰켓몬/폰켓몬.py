def solution(nums):
    num_types = len(set(nums)) #set = 포켓몬의 종류를 구합니다.
    num_to_select = len(nums) // 2  #선택해야할 포켓몬의 수
    return min(num_types, num_to_select)