def solution(arr1, arr2):
    len_arr1, len_arr2 = len(arr1), len(arr2)  # 두 배열의 길이를 구합니다.

    # 두 배열의 길이를 비교합니다.
    if len_arr1 > len_arr2:
        return 1
    elif len_arr1 < len_arr2:
        return -1

    # 두 배열의 길이가 같은 경우, 배열의 원소들의 합을 비교합니다.
    sum_arr1, sum_arr2 = sum(arr1), sum(arr2)
    if sum_arr1 > sum_arr2:
        return 1
    elif sum_arr1 < sum_arr2:
        return -1

    # 두 배열의 길이와 원소들의 합이 모두 같은 경우
    return 0
