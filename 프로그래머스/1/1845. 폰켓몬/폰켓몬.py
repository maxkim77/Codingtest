def solution(nums):
    nums_type = len(set(nums))
    nums_to_select = len(nums) // 2
    return min(nums_type, nums_to_select)

#최대한 많은 종류의 포켓몬 종류 N/2
#모든 포켓몬종류
#min